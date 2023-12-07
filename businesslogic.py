import os
import sys
import time
import json
import yaml
import logging
import decimal
import babel.numbers
from pygame import mixer
from PySide6.QtCore import QObject, Slot, QRunnable

from path import Pathinfo
from appinfo import Info
from signals import GameFinderSignals, WorkerSignals, SettingsSignals

from ebaysdk.finding import Connection as FindingConnection
from ebaysdk.exception import ConnectionError

class GameFinder(FindingConnection, QObject):
    def __init__(self):
        self.signals = GameFinderSignals()

        self.pathinfo = Pathinfo()

        self.settings = Settings()
        self.settings.signals.reload.connect(self.settings.load)
        self.settings.load()

        # Initialize pygame audio mixer
        mixer.init()

        super(GameFinder, self).__init__(config_file = self.pathinfo.ebay)

    def find(self):
        self.running = True

        with open(self.pathinfo.platforms, "r") as fd:
            platform_config = yaml.load(fd, Loader=yaml.SafeLoader)

        try:
            for platform in platform_config:
                api_request = {
                    'keywords': '',
                    'categoryId': '',
                    'sortOrder': 'StartTimeNewest',
                    'aspectFilter': [],
                    'itemFilter': [],
                }

                platform_yaml = os.path.join(self.pathinfo.app, "%s.txt" % (platform,))

                check = platform_config[platform].get('categoryId')
                if check != None:
                    api_request['categoryId'] = check
                else:
                    logging.critical("categoryId is required")
                    sys.exit(0)

                check = platform_config[platform].get('keywords')
                if check != None:
                    api_request['keywords'] = check

                check = platform_config[platform].get('sortOrder')
                if check != None:
                    api_request['sortOrder'] = check

                # itemFilters
                for key in platform_config[platform].get('itemFilters', []):
                    api_request['itemFilter'].append({'name': key, 'value': platform_config[platform]['itemFilters'][key]})

                # aspectFilters
                for key in platform_config[platform].get('aspectFilters', []):
                    for value in platform_config[platform]['aspectFilters'][key]:
                        api_request['aspectFilter'].append({'aspectName': key, 'aspectValueName': value})

                # send API request
                response = self.execute('findItemsAdvanced', api_request)
                j = json.loads(response.json())

                if j['ack'] != 'Success':
                    logging.error("Search failed")
                    logging.error("{}".format(str(response.json())))
                    continue

                if int(j['searchResult']['_count']) < 1:
                    logging.info("No search results found for category '{}'".format(platform_config[platform].get('categoryId')))
                    continue

                latest_auction_stamp = j['searchResult']['item'][0]['listingInfo']['startTime']
                latest_timestamp = time.mktime(time.strptime(latest_auction_stamp, "%Y-%m-%dT%H:%M:%S.%fZ"))
                last_timestamp = 0

                if os.path.exists(platform_yaml):
                    fd = open(platform_yaml, "r")
                    last_auction_stamp = fd.read(24)
                    last_timestamp = time.mktime(time.strptime(last_auction_stamp, "%Y-%m-%dT%H:%M:%S.%fZ"))
                    fd.close()

                if latest_timestamp - last_timestamp > 0:
                    fd = open(platform_yaml, "w")
                    fd.write(latest_auction_stamp)
                    fd.close()

                items = []
                datas = []

                # Loop over list in reverse order since the output is a FIFO and we want the newest entry on top
                for item in reversed(j['searchResult']['item']):
                    current_auction_stamp = item['listingInfo']['startTime']
                    current_timestamp = time.mktime(time.strptime(current_auction_stamp, "%Y-%m-%dT%H:%M:%S.%fZ"))

                    if current_timestamp > last_timestamp:
                        datas.append([
                            item['itemId'],
                            item['title'],
                            # Note that locale is required.
                            # Otherwise you will see this https://github.com/python-babel/babel/issues/977
                            babel.numbers.format_currency(decimal.Decimal(item['sellingStatus']['currentPrice']['value']), item['sellingStatus']['currentPrice']['_currencyId'], locale='en_US'),
                            item['sellingStatus']['currentPrice']['_currencyId'],
                            item['listingInfo']['bestOfferEnabled'],
                            item['listingInfo']['buyItNowAvailable'],
                            item['viewItemURL'],
                        ])
                        items.append(item['title'])

                itemCount = len(items)

                # Audio Notification
                if self.settings.enableAudioNotification and itemCount > 0:
                    mixer.music.load(self.pathinfo.music.games)
                    if not mixer.get_busy():
                        mixer.music.play()

                # Desktop Notifcation
                if self.settings.enableDesktopNotification and itemCount > 0:
                    notification = "Found {} items".format(itemCount)
                    for i in items[0:2]:
                        notification += "\n{}".format(i)
                    self.signals.notify.emit((Info.APPNAME, notification))

                self.signals.data.emit(datas)

        except ConnectionError as e:
            logging.error(e)
            logging.error("{}".format(str(e)))

class Worker(QRunnable):
    def __init__(self):
        super(Worker, self).__init__()
        self.running = False
        self.signals = WorkerSignals()
        self.pathinfo = Pathinfo()
        self.settings = Settings()
        self.settings.signals.reload.connect(self.settings.load)
        self.settings.load()

    def handleGameFinderNotify(self, t):
        self.signals.notify.emit(t)

    def handleGameFinderData(self, d):
        self.signals.data.emit(d)

    @Slot()
    def run(self):
        self.running = True
        if os.path.exists(self.pathinfo.ebay) and os.path.exists(self.pathinfo.platforms):
            gf = GameFinder()
            gf.signals.notify.connect(self.handleGameFinderNotify)
            gf.signals.data.connect(self.handleGameFinderData)

            while self.running:
                gf.find()
                count = 0

                interval = int(self.settings.automaticIntervalTime)

                if self.settings.automaticInterval:
                    # Calculate interval in 60 second blocks
                    # and auto determine how often we should 
                    # sleep before another run.
                    with open(self.pathinfo.platforms, "r") as fd:
                        platforms = yaml.load(fd, Loader=yaml.SafeLoader)
                        platformCount = len(platforms.keys())
                    
                    if platformCount > 0:
                        maxApiCallsPerPlatform = int(self.settings.apiCallsPerDay) / int(platformCount)

                        interval = 0
                        seconds = 60
                        maxSecondsPerPlatforms = 0

                        while maxSecondsPerPlatforms < 86400:
                            interval += 1
                            maxSecondsPerPlatforms = maxApiCallsPerPlatform * seconds * interval
                    else:
                        # no platforms to monitor, default to interval of 1 minute
                        interval = 1

                while self.running and count < 60 * interval * 4:
                    time.sleep(0.25)
                    count += 1
        return

    def stop(self):
        self.running = False

    def isRunning(self):
        return(self.running)

class Conditions:
    def __init__(self):
        self.pathinfo = Pathinfo()
        with open(self.pathinfo.itemfilters, "r") as fd:
            data = yaml.load(fd, Loader=yaml.SafeLoader)
            self.conditions = data['Condition']

class SavedPlatforms:
    def __init__(self):
        self.itemfilters = False
        self.aspectfilters = False
        self.saved = False
        self.pathinfo = Pathinfo()
        self.load()

    def load(self):
        try:
            with open(self.pathinfo.platforms, "r") as fd:
                self.saved = yaml.load(fd, Loader=yaml.SafeLoader)
        except:
            self.saved = {}

        try:
            with open(self.pathinfo.itemfilters, "r") as fd:
                self.itemfilters = yaml.load(fd, Loader=yaml.SafeLoader)
        except:
            self.itemfilters = {}

        try:
            with open(self.pathinfo.aspectfilters, "r") as fd:
                self.aspectfilters = yaml.load(fd, Loader=yaml.SafeLoader)
        except:
            self.aspectfilters = {}

    def reload(self):
        self.load()

    def search(self, id):
        try:
            keywords = self.saved[id]['keywords']
        except:
            keywords = None
        return(keywords)

    def conditionIds(self, id):
        try:
            conditions = self.saved[id]['itemFilters']['Conditions']
        except Exception as e:
            conditions = []
        return conditions

    def conditionNames(self, id):
        conditionNames = []
        for conditionId in self.conditionIds(id):
            for condition in self.itemfilters['Condition'].keys():
                if self.itemfilters['Condition'][condition] == conditionId:
                    conditionNames.append(condition)
        return(conditionNames)

    def location(self, id):
        try:
            location = self.saved[id]['itemFilters']['LocatedIn']
        except:
            location = []
        return location

    def aspectFilterTypes(self, id):
        return self.saved[id]['aspectFilters'].keys()

    def platform(self, id, isCategoryId = False):
        if isCategoryId:
            return self.aspectfilters[id]['aspectFilters']['Platform']
        return self.saved[id]['aspectFilters']['Platform']

    def model(self, id, isCategoryId = False):
        if isCategoryId:
            return self.aspectfilters[id]['aspectFilters']['Model']
        return self.saved[id]['aspectFilters']['Model']

    def categoryId(self, id):
        return self.saved[id]['categoryId']

    def category(self, id):
        return self.aspectfilters[self.categoryId(id)]['name']
    
    def get(self):
        return(self.saved)

    def ids(self):
        return(self.saved.keys())

class Settings:
    apiCallsPerDay = 5000
    automaticInterval = True
    automaticIntervalTime = 1
    searchOnStartup = False
    enableAudioNotification = True
    enableDesktopNotification = True

    signals = SettingsSignals()

    def __init__(self):
        self.pathinfo = Pathinfo()
        # create settings.yaml with defaults if it does not exist
        if not os.path.exists(self.pathinfo.settings):
            save = {
                'apiCallsPerDay': self.apiCallsPerDay,
                'automaticInterval': self.automaticInterval,
                'automaticIntervalTime': self.automaticIntervalTime,
                'searchOnStartup': self.searchOnStartup,
                'enableAudioNotification': self.enableAudioNotification,
                'enableDesktopNotification': self.enableDesktopNotification,
            }
            with open(self.pathinfo.settings, "w") as fd:
                yaml.dump(save, fd)

    def load(self):
        with open(self.pathinfo.settings, "r") as fd:
            settings = yaml.load(fd, Loader=yaml.SafeLoader)
            self.apiCallsPerDay = settings['apiCallsPerDay']
            self.automaticInterval = settings['automaticInterval']
            self.automaticIntervalTime = settings['automaticIntervalTime']
            self.searchOnStartup = settings['searchOnStartup']
            self.enableAudioNotification = settings['enableAudioNotification']
            self.enableDesktopNotification = settings['enableDesktopNotification']

    def save(self):
        with open(self.pathinfo.settings, "r") as fd:
            settings = yaml.load(fd, Loader=yaml.SafeLoader)
        
        save = {
            'apiCallsPerDay': self.apiCallsPerDay,
            'automaticInterval': self.automaticInterval,
            'automaticIntervalTime': self.automaticIntervalTime,
            'searchOnStartup': self.searchOnStartup,
            'enableAudioNotification': self.enableAudioNotification,
            'enableDesktopNotification': self.enableDesktopNotification,
        }

        with open(self.pathinfo.settings, "w") as fd:
            yaml.dump(save, fd)

        self.signals.reload.emit(True)