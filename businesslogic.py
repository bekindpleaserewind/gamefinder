import os
import sys
import time
import json
import yaml
import decimal
import babel.numbers
from pygame import mixer
from PySide6.QtCore import QObject, Slot, QRunnable

from appinfo import Info
from signals import GameFinderSignals, WorkerSignals

sys.path.insert(0, '%s' % os.path.dirname(__file__))
from ebaysdk.finding import Connection as FindingConnection
from ebaysdk.exception import ConnectionError


class GameFinder(FindingConnection, QObject):
    def __init__(self):
        self.signals = GameFinderSignals()

        self.settings = Settings()
        self.settings.load()

        self.config = os.path.join(os.environ['APPDATA'], Info.APPNAME, 'ebay.yaml')
        self.platforms = os.path.join(os.environ['APPDATA'], Info.APPNAME, 'platforms.yaml')

        # Initialize pygame audio mixer
        mixer.init()

        super(GameFinder, self).__init__(config_file = self.config)

    def find(self):
        self.running = True

        with open(self.platforms, "r") as fd:
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

                platform_yaml = os.path.join(os.environ['APPDATA'], Info.APPNAME, "%s.txt" % (platform,))

                check = platform_config[platform].get('categoryId')
                if check != None:
                    api_request['categoryId'] = check
                else:
                    print("categoryId is required")
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
                    print("Search failed")
                    print(str(response.json()))
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
                            babel.numbers.format_currency(decimal.Decimal(item['sellingStatus']['currentPrice']['value']), item['sellingStatus']['currentPrice']['_currencyId']),
                            item['sellingStatus']['currentPrice']['_currencyId'],
                            item['listingInfo']['bestOfferEnabled'],
                            item['listingInfo']['buyItNowAvailable'],
                            item['viewItemURL'],
                        ])
                        items.append(item['title'])

                itemCount = len(items)
                # Audio Notification
                if self.settings.enableAudioNotification and itemCount > 0:
                    song = os.path.join(sys._MEIPASS, 'alerts', "games.mp3")
                    mixer.music.load(song)

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
            print(e)
            print(e.response.dict())

class Worker(QRunnable):
    def __init__(self):
        super(Worker, self).__init__()
        self.running = False
        self.signals = WorkerSignals()

    def handleGameFinderNotify(self, t):
        self.signals.notify.emit(t)

    def handleGameFinderData(self, d):
        self.signals.data.emit(d)

    @Slot()
    def run(self):
        self.running = True
        if Info.FROZEN:
            self.config = os.path.join(os.environ['APPDATA'], Info.APPNAME, 'ebay.yaml')
            self.platforms = os.path.join(os.environ['APPDATA'], Info.APPNAME, 'platforms.yaml')
            
        if os.path.exists(self.config) and os.path.exists(self.platforms):
            gf = GameFinder()
            gf.signals.notify.connect(self.handleGameFinderNotify)
            gf.signals.data.connect(self.handleGameFinderData)

            while self.running:
                gf.find()
                count = 0
                while self.running and count < 60 * 4:
                    time.sleep(0.25)
                    count += 1

        return

    def stop(self):
        self.running = False

    def isRunning(self):
        return(self.running)

class Conditions:
    def __init__(self):
        with open(os.path.join(sys._MEIPASS, 'itemfilters.yaml'), "r") as fd:
            data = yaml.load(fd, Loader=yaml.SafeLoader)
            self.conditions = data['Condition']

class SavedPlatforms:
    def __init__(self):
        self.itemfilters = False
        self.aspectfilters = False
        self.saved = False

        self.load()

    def load(self):
        try:
            with open(os.path.join(os.environ['APPDATA'], Info.APPNAME, 'platforms.yaml'), "r") as fd:
                self.saved = yaml.load(fd, Loader=yaml.SafeLoader)
        except:
            self.saved = {}

        try:
            with open(os.path.join(sys._MEIPASS, 'itemfilters.yaml'), "r") as fd:
                self.itemfilters = yaml.load(fd, Loader=yaml.SafeLoader)
        except:
            self.itemfilters = {}

        try:
            with open(os.path.join(sys._MEIPASS, 'aspectfilters.yaml'), "r") as fd:
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
            conditions = [self.saved[id]['itemFilters']['Condition']]
        except:
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
            location = [self.saved[id]['itemFilters']['LocatedIn']]
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

    def __init__(self):
        # create settings.yaml with defaults if it does not exist
        if not os.path.exists(os.path.join(os.environ['APPDATA'], Info.APPNAME, 'settings.yaml')):
            save = {
                'apiCallsPerDay': self.apiCallsPerDay,
                'automaticInterval': self.automaticInterval,
                'automaticIntervalTime': self.automaticIntervalTime,
                'searchOnStartup': self.searchOnStartup,
                'enableAudioNotification': self.enableAudioNotification,
                'enableDesktopNotification': self.enableDesktopNotification,
            }
            with open(os.path.join(os.environ['APPDATA'], Info.APPNAME, 'settings.yaml'), "w") as fd:
                yaml.dump(save, fd)

    def load(self):
        with open(os.path.join(os.environ['APPDATA'], Info.APPNAME, 'settings.yaml'), "r") as fd:
            settings = yaml.load(fd, Loader=yaml.SafeLoader)
            self.apiCallsPerDay = settings['apiCallsPerDay']
            self.automaticInterval = settings['automaticInterval']
            self.automaticIntervalTime = settings['automaticIntervalTime']
            self.searchOnStartup = settings['searchOnStartup']
            self.enableAudioNotification = settings['enableAudioNotification']
            self.enableDesktopNotification = settings['enableDesktopNotification']

    def save(self):
        with open(os.path.join(os.environ['APPDATA'], Info.APPNAME, 'settings.yaml'), "r") as fd:
            settings = yaml.load(fd, Loader=yaml.SafeLoader)
        
        save = {
            'apiCallsPerDay': self.apiCallsPerDay,
            'automaticInterval': self.automaticInterval,
            'automaticIntervalTime': self.automaticIntervalTime,
            'searchOnStartup': self.searchOnStartup,
            'enableAudioNotification': self.enableAudioNotification,
            'enableDesktopNotification': self.enableDesktopNotification,
        }

        with open(os.path.join(os.environ['APPDATA'], Info.APPNAME, 'settings.yaml'), "w") as fd:
            yaml.dump(save, fd)