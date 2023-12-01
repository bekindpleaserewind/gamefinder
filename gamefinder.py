# -*- coding: utf-8 -*-
import pprint
import os
import sys
import signal
import yaml
import uuid

import iso3166

from PySide6.QtGui import QIcon, QAction, QColor, QDesktopServices
from PySide6.QtCore import QThreadPool, QSize, Qt
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QMainWindow, QWidget, QHBoxLayout, QLabel, QHeaderView, QTableWidget, QTableWidgetItem, QAbstractItemView, QSizePolicy, QDialog, QComboBox, QTreeWidgetItem, QButtonGroup

from appinfo import Info
from signals import AppSignals
from businesslogic import GameFinder, Worker, Conditions, SavedPlatforms, Settings

from mainwindow import Ui_MainWindow
from setupwizard import SetupWizard
from toolbarspacer import Ui_toolBarSpacer
from widgetmin import Ui_widgetmin
from widgetsaved import Ui_widgetsaved
from platforms import Ui_Platforms
from settings import Ui_Settings
from about import Ui_About

OFFLINE = 0
ONLINE = 1

TYPE_CATEGORY = 0
TYPE_ID = 1
TYPE_ITEM = 2


def handler(signum, frame):
    pass

class App:
    def __init__(self, qtApp, foreground = False):
        self.app = qtApp
        self.signals = AppSignals()
        self.worker = None
        self.threadpool = None

    def run(self):
        self.threadpool = QThreadPool()
        self.worker = Worker()
        self.worker.signals.notify.connect(self.handleSignalWorkerNotify)
        self.worker.signals.data.connect(self.handleSignalWorkerData)
        self.threadpool.start(self.worker)

    def handleSignalWorkerNotify(self, t):
        self.signals.notify.emit(t)

    def handleSignalWorkerData(self, d):
        self.signals.data.emit(d)

    def stop(self):
        if self.worker is not None and self.worker.isRunning():
            self.worker.stop()

    def wait(self):
        if self.threadpool is not None:
            self.threadpool.waitForDone()

class SystemTrayIcon(QSystemTrayIcon):
    def __init__(self, icon: QIcon, gamefinder: GameFinder, window: QMainWindow, *args, **kwargs):
        super(SystemTrayIcon, self).__init__()
        self.window = window
        self.setIcon(icon)
        self.setVisible(True)
        self.menu = QMenu()
        self.quit = QAction("Quit")
        self.menu.addAction(self.quit)
        self.quit.triggered.connect(window.shutdown)
        self.setContextMenu(self.menu)

        self.activated.connect(self.swapWindow)
        self.messageClicked.connect(self.showWindow)
    
    def swapWindow(self, reason):
        if reason != self.ActivationReason.Context:
            if self.window.isHidden():
                self.window.show()
            elif self.window.isVisible():
                self.window.hide()

    def showWindow(self, *args, **kwargs):
        if self.window.isHidden():
            self.window.show()
        
class ToolBarSpacer(QWidget, Ui_toolBarSpacer):
    def __init__(self):
        super(ToolBarSpacer, self).__init__()
        self.setupUi(self)


class IconStatusBar(QWidget, Ui_widgetmin):
    def __init__(self, state):
        super(IconStatusBar, self).__init__()
        self.setupUi(self)

        if state == ONLINE:
            self.icon = QIcon(os.path.join(sys._MEIPASS, 'online.png'))
        elif state == OFFLINE:
            self.icon = QIcon(os.path.join(sys._MEIPASS, 'online.png'))
        else:
            return

        self.pixmap = self.icon.pixmap(QSize(12,12))

        self.iconLayout = QHBoxLayout()
        self.iconLayout.addStretch()

        self.label = QLabel()
        self.label.setFixedHeight(12)
        self.label.setWindowFlag(Qt.FramelessWindowHint)
        self.label.setPixmap(self.pixmap)
        self.iconLayout.addWidget(self.label)

        self.labelText = QLabel()
        self.labelText.setFixedHeight(12)
        self.labelText.setWindowFlag(Qt.FramelessWindowHint)

        if state == OFFLINE:
            self.labelText.setText("Offline")
        elif state == ONLINE:
            self.labelText.setText("Online")

        self.iconLayout.addWidget(self.labelText)

        self.setLayout(self.iconLayout)

class LinkWidget(QWidget):
    def __init__(self, url, color, items, parent = None):
        super(LinkWidget, self).__init__(parent)
        self.items = items
        self.linkLayout = QHBoxLayout()
        self.linkLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.linkLayout)

        self.link = QLabel(self)
        self.link.setContentsMargins(0, 0, 0, 0)
        self.link.setStyleSheet("background-color: {}".format(color))
        self.link.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        #self.link.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.link.setOpenExternalLinks(False)
        self.link.setText("<a href=\"{}\">{}</a>".format(url, url))
        self.link.setAutoFillBackground(True)
        self.linkLayout.addWidget(self.link)
        self._lastpos = None

        self.link.linkActivated.connect(self.handleLinkActivated)

    def handleLinkActivated(self, link):
        # Scan table for this object (self)
        color = self.getColorFromHex("FFFFFF")
        table = self.parent().parent()

        for row in range(0, table.rowCount()):
            if table.cellWidget(row, 6) == self:
                table.setCurrentCell(row, 6)
                # Clear background for cells not including Location
                for col in range(0, 6):
                    item = table.item(row, col)
                    item.setBackground(color)
                break
        
        # Clear url cell background
        self.clearBackground()

        # Open link with desktop default browser
        QDesktopServices.openUrl(link)

    def clearBackground(self):
        self.link.setStyleSheet("background-color: {}".format('#ffffff'))

    def mouseReleaseEvent(self, event):
        qpointf = event.position()
        clickedWidget = self.childAt(qpointf.toPoint())
        clickedWidgetParent = clickedWidget.parent()
        clickedWidgetParent.clearBackground()

        table = clickedWidgetParent.parent().parent()
        clickedWidgetParentPosition = clickedWidgetParent.pos()
        item = table.indexAt(clickedWidgetParentPosition)
        row = item.row()
        color = self.getColorFromHex("FFFFFF")

        for col in range(0, 6):
            item = table.item(row, col)
            item.setBackground(color)

    def getColorFromHex(self, hex):
        rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
        color = QColor.fromRgb(rgb[0], rgb[1], rgb[2])
        return(color)

class TableWidget(QTableWidget):
    def __init__(self, parent = None):
        super(TableWidget, self).__init__(parent)
        self._data = []

        self._headers = ['ID', 'Title', 'Price', 'Currency', 'Best Offer', 'Buy it Now', 'Location']
        self.setColumnCount(len(self._headers))
        self.setHorizontalHeaderLabels(self._headers)

        # Hide the vertical header column
        self.verticalHeader().hide()

        # Disable highlighting/focus/editing cells
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # Setup resizing of each collumn
        self.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeMode.Stretch)
        
        # Handle signals
        self.cellClicked.connect(self.handleCellClicked)

    def handleCellClicked(self, row, column = None):
        items = []
        for i in range(0, 6):
            items.append(self.item(row, i))

        color = self.getColorFromHex("FFFFFF")

        for item in items:
            if item:
                item.setBackground(color)

        widget = self.cellWidget(row, 6)
        if widget:
            widget.clearBackground()

        
    def getItemsFromRow(self, row):
        itemId = self.item(row, 0)
        title = self.item(row, 1)
        price = self.item(row, 2)
        currency = self.item(row, 3)
        bestOffer = self.item(row, 4)
        buyItNow = self.item(row, 5)
        link = self.item(row, 6)
        return((itemId, title, price, currency, bestOffer, buyItNow, link))

    def addData(self, data = []):
        self._data = data + self._data

        for i in range(0, len(data)):
            self.insertRow(0)
            row = self.generateRow(data[i])
            self.setItem(0, 0, row[0])
            self.setItem(0, 1, row[1])
            self.setItem(0, 2, row[2])
            self.setItem(0, 3, row[3])
            self.setItem(0, 4, row[4])
            self.setItem(0, 5, row[5])
            self.setCellWidget(0, 6, row[6])

    def getColorFromHex(self, hex):
        rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
        color = QColor.fromRgb(rgb[0], rgb[1], rgb[2])
        return(color)

    def generateRow(self, row):
        color = self.getColorFromHex("ebcb17")
        itemId = QTableWidgetItem(row[0])
        itemId.setBackground(color)
        title = QTableWidgetItem(row[1])
        title.setBackground(color)
        price = QTableWidgetItem(row[2]) 
        price.setBackground(color)
        currency = QTableWidgetItem(row[3])
        currency.setBackground(color)
        bestOffer = QTableWidgetItem(row[4])
        bestOffer.setBackground(color)
        buyItNow = QTableWidgetItem(row[5])
        buyItNow.setBackground(color)
        link = LinkWidget(row[6], "#ebcb17", [itemId, title, price, currency, bestOffer, buyItNow], self)

        return((itemId, title, price, currency, bestOffer, buyItNow, link))

    def markResultsRead(self):
        for row in range(0, len(self._data)):
            self.handleCellClicked(row)

class WidgetSaved(QWidget, Ui_widgetsaved):
    def __init__(self):
        super(WidgetSaved, self).__init__()
        self.setupUi(self)
        self.body.setColumnCount(1)
    

class Platform:
    search = {}
    category = {}
    locations = {}
    conditions = {}
    platforms = {}
    models = {}

    def addPlatform(self, search, category, locations, conditions, platform = None, model = None):
        id = str(uuid.uuid4())
        self.search[id] = search
        self.category[id] = category
        self.platforms[id] = platform
        self.models[id] = model
        self.locations[id] = locations
        self.conditions[id] = conditions
        
        config = {}
        if os.path.exists(os.path.join(os.environ['APPDATA'], Info.APPNAME, 'platforms.yaml')):
            with open(os.path.join(os.environ['APPDATA'], Info.APPNAME, 'platforms.yaml'), "r") as fd:
                config = yaml.load(fd, Loader=yaml.SafeLoader)

        config[id] = {
            'categoryId': self.category[id],
            'keywords': self.search[id],
            'sortOrder': 'StartTimeNewest',
            'aspectFilters': {},
            'itemFilters': {},
        }

        if category == 139973 and self.platforms[id] is not None:
            config[id]['aspectFilters']['Platform'] = self.platforms[id]
        elif category == 260000 and self.models[id] is not None:
            config[id]['aspectFilters']['Model'] = self.models[id]

        if len(self.locations[id]) > 0:
            config[id]['itemFilters']['LocatedIn'] = self.locations[id]
        if len(self.conditions[id]) > 0:
            config[id]['itemFilters']['Conditions'] = self.conditions[id]
        
        with open(os.path.join(os.environ['APPDATA'], Info.APPNAME, 'platforms.yaml'), "w") as fd:
            yaml.dump(config, fd)

        return(id)

class AboutDialog(QDialog, Ui_About):
    def __init__(self, parent = None):
        super(AboutDialog, self).__init__(parent)
        self.setupUi(self)
        icon = QIcon(os.path.join(sys._MEIPASS, 'gamefinder_logo_whitebackground.png'))
        pixmap = icon.pixmap(QSize(128, 128))
        self.logo.setPixmap(pixmap)

class PlatformsDialog(QDialog, Ui_Platforms):
    def __init__(self, parent = None):
        super(PlatformsDialog, self).__init__()
        self.categoryToPlatform = {}
        self.categoryToItemFilters = {}
        self.categoryToAspectFilters = {}
        self.setupUi(self)

        self.results = []
        self.saves = False
        self.clickTracker = False

        # Track the number of items
        self.platformComboItemCount = 0
        self.modelComboItemCount = 0
        self.locationComboItemCount = 0
        self.conditionComboItemCount = 0

        # Track how many checkboxes have been checked
        self.countLocations = 0

        # Setup UI customizations and defaults
        self.platforms.hide()
        self.platformsLabel.hide()
        self.models.hide()
        self.modelsLabel.hide()
        self.platforms.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.models.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.category.addItem("Select a Category", userData=False)

        self.loadCategory()
        self.loadConditions()
        self.loadLocations()

        self.category.model().itemChanged.connect(self.categoryItemChanged)
        self.locations.model().itemChanged.connect(self.locationItemChanged)
        self.platforms.model().itemChanged.connect(self.platformsItemChanged)
        self.models.model().itemChanged.connect(self.modelsItemChanged)
        self.conditions.model().itemChanged.connect(self.conditionsItemChanged)

        self.create.clicked.connect(self.createClicked)
        self.remove.clicked.connect(self.removeClicked)

        self.loadSaved()

    def loadSaved(self):
        if self.saves:
            self.loadCategory(False)
            self.saves.reload()
        else:
            self.saves = SavedPlatforms()

        items = {}
        for configId in self.saves.ids():
            items[configId] = {
                'search': self.saves.search(configId),
                'category': self.saves.category(configId),
                'locations': self.saves.location(configId),
            }

            # Add the conditions (defaults to Any Condition)
            conditions = self.saves.conditionNames(configId)
            if len(conditions) > 0:
                items[configId]['conditions'] = conditions
            else:
                items[configId]['conditions'] = ["Any Condition"]

            # Generate supported aspectFilters configuration
            for aspectFilterType in self.saves.aspectFilterTypes(configId):
                if aspectFilterType == "Platform":
                    items[configId]['platforms'] = self.saves.platform(configId)
                elif aspectFilterType == "Model":
                    items[configId]['models'] = self.saves.model(configId)
                else:
                    print("Aspect filter '{}' not supported".format(aspectFilterType))

        self.root.clear()
        self.root.setSelectionBehavior(QAbstractItemView.SelectRows)

        roots = {}
        for configId in items.keys():
            root = roots.get(items[configId]['category'])
            if not root:
                root = QTreeWidgetItem([items[configId]['category']])
                root.setData(0, Qt.UserRole, TYPE_CATEGORY)
                roots[items[configId]['category']] = root

            id = QTreeWidgetItem([str(configId), ""])
            id.setData(0, Qt.UserRole, TYPE_ID)

            search = QTreeWidgetItem(["Keywords", str(items[configId]['search'])], )
            search.setData(0, Qt.UserRole, TYPE_ITEM)
            locations = QTreeWidgetItem(["Locations", str(items[configId]['locations'])])
            locations.setData(0, Qt.UserRole, TYPE_ITEM)
            conditions = QTreeWidgetItem(["Conditions", str(items[configId]['conditions'])])
            conditions.setData(0, Qt.UserRole, TYPE_ITEM)

            for aspectFilterType in self.saves.aspectFilterTypes(configId):
                if aspectFilterType == "Platform":
                    platforms = QTreeWidgetItem(["Platforms", str(items[configId]['platforms'])])
                    platforms.setData(0, Qt.UserRole, TYPE_ITEM)
                elif aspectFilterType == "Model":
                    models = QTreeWidgetItem(["Models", str(items[configId]['models'])])
                    models.setData(0, Qt.UserRole, TYPE_ITEM)


            root.addChild(id)
            id.addChild(search)
            id.addChild(locations)
            id.addChild(conditions)
            for aspectFilterType in self.saves.aspectFilterTypes(configId):
                if aspectFilterType == "Platform":
                    id.addChild(platforms)
                elif aspectFilterType == "Model":
                    id.addChild(models)

        for rootLevelItem in roots.keys():
            self.root.addTopLevelItem(roots[rootLevelItem])
        
        self.root.expandAll()
        self.root.resizeColumnToContents(0)
        self.root.resizeColumnToContents(1)
        self.root.itemClicked.connect(self.highlightClickedIdRow)
    
    def highlightClickedIdRow(self, item, column):
        targets = self.getTargetsFromLoadedSaves(self.root)
        for target in targets:
            target.setSelected(True)

    def createClicked(self):
        search = self.search.text()

        currentData = self.category.currentData()
        if currentData:
            category = currentData[0]
            if not category:
                print("No Category Selected")
                return False
        
            if category == 139973:
                platforms = self.getPlatforms()
                if len(platforms) == 0:
                    print("No Platforms Selected")
                    return False
            elif category == 260000:
                models = self.getModels()
                if len(models) == 0:
                    print("No Models Selected")
                    return False

            locations = self.getLocations()
            if len(locations) == 0:
                print("No locations selected")
                return False

            conditions = []
            tmpConditions = self.getConditions()
            for condition in tmpConditions:
                # Remove all conditions if Any condition is specified
                if condition == -1:
                    conditions = []
                    break
                else:
                    conditions.append(condition)

            result = Platform()
            if category == 139973:
                result.addPlatform(search, category, locations, conditions, platform = platforms)
            else:
                result.addPlatform(search, category, locations, conditions, model = models)

            self.resetUi()
            self.loadSaved()

    def resetUi(self):
        self.platforms.clear()
        self.platforms.hide()
        self.platformsLabel.hide()
        self.models.clear()
        self.models.hide()
        self.modelsLabel.hide()

        self.platforms.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.models.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.search.clear()
        self.search.setFocus()

        self.category.clear()
        self.category.addItem("Select a Category", userData=False)

        self.loadCategory()
        self.loadConditions(True)
        self.loadLocations(True)

    def removeClicked(self):
        targets = self.getTargetsFromLoadedSaves(self.root)
        for target in targets:
            targetType = target.data(0, Qt.UserRole)
            if targetType == TYPE_ID:
                configId = target.text(0)
                with open(os.path.join(os.environ['APPDATA'], Info.APPNAME, 'platforms.yaml'), "r") as fd:
                    config = yaml.load(fd, Loader=yaml.SafeLoader)

                with open(os.path.join(os.environ['APPDATA'], Info.APPNAME, 'platforms.yaml'), "w") as fd:
                    del config[configId]
                    yaml.dump(config, fd)

                # Only need to delete TYPE_ID
                self.resetUi()
                self.loadSaved()
                return True

        return False

    def getTargetsFromLoadedSaves(self, root):
        targets = []
        item = root.currentItem()
        if item is not None:
            itemType = item.data(0, Qt.UserRole)

            if itemType == TYPE_CATEGORY:
                item.setSelected(False)
            elif itemType == TYPE_ID:
                targets.append(item)
                for n in range(0, item.childCount()):
                        child = item.child(n)
                        targets.append(child)
            elif itemType == TYPE_ITEM:
                parent = item.parent()
                targets.append(parent)

                for n in range(0, parent.childCount()):
                    child = parent.child(n)
                    targets.append(child)
            else:
                print("Invalid Item Type")

        return targets

    def categoryItemChanged(self, item):
        data = item.data(role = Qt.UserRole)
        if not data:
            self.platforms.clear()
            self.platforms.hide()
            self.platformsLabel.hide()
            self.platforms.addItem("Please select a category first", userData=False)
            self.platformComboItemCount = 0
            self.models.clear()
            self.models.hide()
            self.modelsLabel.hide()
            self.models.addItem("Please select a category first", userData=False)
            self.modelComboItemCount = 0

    def locationItemChanged(self, item):
        checked = item.checkState()
        if checked == Qt.Checked:
            if item.index().row() == 0:
                self.clickTracker = True
                item.setCheckState(Qt.Unchecked)
            elif self.countLocations >= 25:
                # Max locations supported by ebay api is 25
                self.clickTracker = True
                item.setCheckState(Qt.Unchecked)
            else:
                self.countLocations += 1
        elif checked == Qt.Unchecked and not self.clickTracker and item.index().row() > 0:
            if self.countLocations > 0:
                self.countLocations -= 1
        elif self.clickTracker:
            self.clickTracker = False

    def platformsItemChanged(self, item):
        self.uncheckItem(item)

    def modelsItemChanged(self, item):
        self.uncheckItem(item)

    def conditionsItemChanged(self, item):
        self.uncheckItem(item)

    def uncheckItem(self, item):
        checked = item.checkState()
        if checked == Qt.Checked:
            # Do not support checking first item (it is informational only)
            if item.index().row() == 0:
                item.setCheckState(Qt.Unchecked)

    def addLocationCheckComboItem(self, item, value, checked = False):
        self.locations.addItem(item, userData=value)
        item = self.locations.model().item(self.locationComboItemCount, 0)
        item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        if checked:
            item.setCheckState(Qt.Checked)
        else:
            item.setCheckState(Qt.Unchecked)
        self.locationComboItemCount += 1

    def addPlatformCheckComboItem(self, item, value):
        self.platforms.addItem(item, userData=value)
        item = self.platforms.model().item(self.platforms.count()-1, 0)
        item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        item.setCheckState(Qt.Unchecked)
        self.platformComboItemCount += 1

    def addModelCheckComboItem(self, item, value):
        self.models.addItem(item, userData=value)
        item = self.models.model().item(self.models.count()-1, 0)
        item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        item.setCheckState(Qt.Unchecked)
        self.modelComboItemCount += 1

    def addConditionsCheckComboItem(self, item, value, setChecked = False):
        self.conditions.addItem(item, userData=value)
        item = self.conditions.model().item(self.conditionComboItemCount, 0)
        item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)

        if setChecked:
            item.setCheckState(Qt.Checked)
        else:
            item.setCheckState(Qt.Unchecked)

        self.conditionComboItemCount += 1

    def loadConditions(self, reset = False):
        if reset:
            self.conditions.clear()
            self.conditionComboItemCount = 0

        self.addConditionsCheckComboItem("Select Conditions", False, False)
        self.addConditionsCheckComboItem("Any Condition", -1, True)

        conditions = Conditions()
        for condition in conditions.conditions.keys():
            self.addConditionsCheckComboItem(condition, conditions.conditions[condition])

    def loadLocations(self, reset = False):
        if reset:
            self.locations.clear()
            self.locationComboItemCount = 0

        self.addLocationCheckComboItem("Select Locations", False)
        self.addLocationCheckComboItem("World Wide", "WorldWide", True)
        self.addLocationCheckComboItem("North America", "North America")
        self.addLocationCheckComboItem("European", "European")

        for country in iso3166.countries:
            self.addLocationCheckComboItem(country.name, country.alpha2)
    
    def loadCategory(self, loadUi = True):
        self.categoryToAspectFilters = {}

        if os.path.exists(os.path.join(os.environ['APPDATA'], Info.APPNAME, 'platforms.yaml')):
            # Load configuration id
            with open(os.path.join(os.environ['APPDATA'], Info.APPNAME, 'platforms.yaml'), 'r') as fd:
                configData = yaml.safe_load(fd)
                for configId in configData:
                    self.categoryToAspectFilters[configId]  = {
                        'aspectFilters': configData[configId]['aspectFilters'],
                    }
            # Load aspectFilter category names and ids
            with open(os.path.join(sys._MEIPASS, 'aspectfilters.yaml'), 'r') as fd:
                aspectFilterData = yaml.safe_load(fd)

                # Get each configuration id
                for configId in self.categoryToAspectFilters.keys():
                    # Get our aspectFilters types we use for each configuration
                    for configDataType in self.categoryToAspectFilters[configId]['aspectFilters'].keys():
                        # Loop over all available aspectFilters and check against aspectFilterDataType
                        for aspectFilterId in aspectFilterData.keys():
                            for aspectFilterType in aspectFilterData[aspectFilterId]['aspectFilters'].keys():
                                if configDataType == aspectFilterType:
                                    # Save the category name
                                    self.categoryToAspectFilters[configId]['categoryIds'] = {aspectFilterId: aspectFilterData[aspectFilterId]['name']}

        # Add categories to UI
        if loadUi:
            categories = {}
            for configId in self.categoryToAspectFilters.keys():
                for categoryId in self.categoryToAspectFilters[configId]['categoryIds'].keys():
                    categories[self.categoryToAspectFilters[configId]['categoryIds'][categoryId]] = [categoryId, configId]
            for category in categories.keys():
                self.category.addItem(category, userData = categories[category])

            # Load any missing categories:
            with open(os.path.join(sys._MEIPASS, 'aspectfilters.yaml'), 'r') as fd:
                aspectFilterData = yaml.safe_load(fd)
                for categoryId in aspectFilterData.keys():
                    name = aspectFilterData[categoryId]['name']
                    if not categories.get(name):
                        # Add missing category
                        self.category.addItem(name, userData = [categoryId, -1])

            self.category.currentIndexChanged.connect(self.updateCategory)
        
    def updateCategory(self, index):
        data = self.category.itemData(index, role = Qt.UserRole)
        if data and data is not None:
            categoryId = self.category.currentData()[0]
            configId = self.category.currentData()[1]

            if categoryId == 139973:
                # Video Games
                #   aspectFilters:
                #       Platform
                self.models.hide()
                self.modelsLabel.hide()
                self.platforms.show()
                self.platformsLabel.show()

                self.platforms.clear()
                self.addPlatformCheckComboItem("Select Platforms", False)

                platforms = self.saves.platform(categoryId, True)
                for item in platforms:
                    if len(item) > 0 and item is not None:
                        self.addPlatformCheckComboItem(item, item)
            elif categoryId == 260000:
                # Video Game & Console Mixed Lots
                #   aspectFilters:
                #       Model
                self.platforms.hide()
                self.platformsLabel.hide()
                self.models.show()
                self.modelsLabel.show()

                self.models.clear()
                self.addModelCheckComboItem("Select Models", False)

                models = self.saves.model(categoryId, True)
                for item in models:
                    if len(item) > 0:
                        self.addModelCheckComboItem(item, item)
            else:
                print("Category '{}' not supported when updating categories".format(categoryId))

    def getPlatforms(self):
        platforms = []
        total = self.platforms.count()
        for index in range(0, total):
            item = self.platforms.model().item(index, 0)
            if item.checkState() == Qt.Checked:
                data = item.data(role = Qt.UserRole)
                if data:
                    platforms.append(data)
        return(platforms)

    def getModels(self):
        models = []
        total = self.models.count()
        for index in range(0, total):
            item = self.models.model().item(index, 0)
            if item.checkState() == Qt.Checked:
                data = item.data(role = Qt.UserRole)
                if data:
                    models.append(data)
        return(models)

    def getConditions(self):
        conditions = []
        total = self.conditions.count()
        for index in range(0, total):
            item = self.conditions.model().item(index, 0)
            if item.checkState() == Qt.Checked:
                data = item.data(role = Qt.UserRole)
                if data:
                    conditions.append(data)
        return(conditions)

    def getLocations(self):
        locations = []
        total = self.locations.count()
        for index in range(0, total):
            item = self.locations.model().item(index, 0)
            if item.checkState() == Qt.Checked:
                data = item.data(role = Qt.UserRole)
                if data:
                    locations.append(data)
        return(locations)

    def accept(self, *args, **kwargs):
        self.hide()

    def reject(self, *args, **kwargs):
        self.hide()

    def getColorFromHex(self, hex):
        rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
        color = QColor.fromRgb(rgb[0], rgb[1], rgb[2])
        return(color)

class SettingsDialog(QDialog, Ui_Settings):
    def __init__(self, parent = None):
        super(SettingsDialog, self).__init__()
        self.toggle = False
        self.intervalMinutes = 1
        self.enableAutomaticIntervals = True

        self.setupUi(self)

        self.automaticIntervalMinutes.setEnabled(False)

        self.automaticIntervalsBg = QButtonGroup()
        self.automaticIntervalsBg.addButton(self.enabledRadioButton)
        self.automaticIntervalsBg.addButton(self.disabledRadioButton)

        self.searchOnStartupBg = QButtonGroup()
        self.searchOnStartupBg.addButton(self.searchOnStartupOn)
        self.searchOnStartupBg.addButton(self.searchOnStartupOff)

        self.enableAudioNotificationBg = QButtonGroup()
        self.enableAudioNotificationBg.addButton(self.enableAudioNotificationOn)
        self.enableAudioNotificationBg.addButton(self.enableAudioNotificationOff)

        self.enableDesktopNotificationBg = QButtonGroup()
        self.enableDesktopNotificationBg.addButton(self.enableDesktopNotificationOn)
        self.enableDesktopNotificationBg.addButton(self.enableDesktopNotificationOff)

        self.buttonBox.accepted.connect(self.accept)
        self.automaticIntervalsBg.buttonClicked.connect(self.checkAutomaticIntervalsButton)
        self.searchOnStartupBg.buttonClicked.connect(self.checkSearchOnStartupButton)
        self.enableAudioNotificationBg.buttonClicked.connect(self.checkEnableAudioNotificationButton)
        self.enableDesktopNotificationBg.buttonClicked.connect(self.checkEnableDesktopNotificationButton)

        # Load Settings object and update in UI
        self.load()

    def checkAutomaticIntervalsButton(self, button):
        if button.text() == "Disabled":
            self.automaticIntervalMinutes.setEnabled(True)
        elif button.text() == "Enabled":
            self.automaticIntervalMinutes.setEnabled(False)
    
    def checkSearchOnStartupButton(self, button):
        if button.text() == "On" and button.isChecked():
            print("Button pressed is {} and checked is {}".format(button.text(), button.isChecked()))
            self.settings.searchOnStartup = True
        else:
            self.settings.searchOnStartup = False

    def checkEnableAudioNotificationButton(self, button):
        if button.text() == "On" and button.isChecked():
            print("Button pressed is {} and checked is {}".format(button.text(), button.isChecked()))
            self.settings.enableAudioNotification = True
        else:
            self.settings.enableAudioNotification = False

    def checkEnableDesktopNotificationButton(self, button):
        if button.text() == "On" and button.isChecked():
            print("Button pressed is {} and checked is {}".format(button.text(), button.isChecked()))
            self.settings.enableDesktopNotification = True
        else:
            self.settings.enableDesktopNotification = False

    def load(self):
        self.settings = Settings()
        self.settings.load()

        self.apiCallsPerDay.setText(str(self.settings.apiCallsPerDay))

        if self.settings.automaticInterval:
            self.enabledRadioButton.setChecked(True)
            self.disabledRadioButton.setChecked(False)
            self.automaticIntervalMinutes.setEnabled(False)
        else:
            self.enabledRadioButton.setChecked(False)
            self.disabledRadioButton.setChecked(True)
            self.automaticIntervalMinutes.setEnabled(True)

        self.automaticIntervalMinutes.setText(str(self.settings.automaticIntervalTime))

        if self.settings.searchOnStartup:
            self.searchOnStartupOn.setChecked(True)
            self.searchOnStartupOff.setChecked(False)
        else:
            self.searchOnStartupOn.setChecked(False)
            self.searchOnStartupOff.setChecked(True)

        if self.settings.enableAudioNotification:
            self.enableAudioNotificationOn.setChecked(True)
            self.enableAudioNotificationOff.setChecked(False)
        else:
            self.enableAudioNotificationOn.setChecked(False)
            self.enableAudioNotificationOff.setChecked(True)
        
        if self.settings.enableDesktopNotification:
            self.enableDesktopNotificationOn.setChecked(True)
            self.enableDesktopNotificationOff.setChecked(False)
        else:
            self.enableDesktopNotificationOn.setChecked(False)
            self.enableDesktopNotificationOff.setChecked(True)

    def accept(self):
        self.settings.apiCallsPerDay = self.apiCallsPerDay.text()

        self.settings.automaticIntervalTime = self.automaticIntervalMinutes.text()
        if self.enabledRadioButton.isChecked():
            self.settings.automaticInterval = True
        else:
            self.settings.automaticInterval = False
        self.settings.save()

        super(SettingsDialog, self).accept()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.running = False

        self.settings = Settings()
        self.settings.load()

        # Set our window icon
        self.setWindowIcon(QIcon(os.path.join(sys._MEIPASS, 'ebay.png')))

        # Create a new gamefinder application and configure signals
        self.gamefinder = App(app)
        self.gamefinder.signals.notify.connect(self.sendNotification)
        self.gamefinder.signals.data.connect(self.updateData)

        # Configure menubar
        self.actionQuit.triggered.connect(self.shutdown)
        self.actionSettings.triggered.connect(self.displaySettingsDialog)
        self.actionToolbar.triggered.connect(self.toolBar.show)
        self.actionPlatforms.triggered.connect(self.displayPlatformsDialog)
        self.actionAuthentication.triggered.connect(self.displayAuthenticationSetup)
        self.actionStart.triggered.connect(self.start)
        self.actionStop.triggered.connect(self.stop)
        self.actionAbout.triggered.connect(self.about)

        # System tray
        self.trayIcon = QIcon(os.path.join(sys._MEIPASS, 'ebay.png'))
        self.tray = SystemTrayIcon(self.trayIcon, self.gamefinder, self)

        # Setup toolbar
        self.toolBar.setIconSize(QSize(24, 24))

        # Toolbar start button
        self.button_start = QAction(QIcon(os.path.join(sys._MEIPASS, 'start.png')), "Start", self)
        self.button_start.setStatusTip("Start Searching")
        self.button_start.triggered.connect(self.start)
        self.button_start.setDisabled(False)
        self.toolBar.addAction(self.button_start)
        # Toolbar stop button
        self.button_stop = QAction(QIcon(os.path.join(sys._MEIPASS, 'stop.png')), "Stop", self)
        self.button_stop.setStatusTip("Stop Searching")
        self.button_stop.triggered.connect(self.stop)
        self.button_stop.setDisabled(True)
        self.toolBar.addAction(self.button_stop)

        self.toolBar.addSeparator()

        # Toolbar tally button
        self.button_clear = QAction(QIcon(os.path.join(sys._MEIPASS, 'tally.png')), "Clear", self)
        self.button_clear.setStatusTip("Mark Results Read")
        self.button_clear.triggered.connect(self.markResultsRead)
        self.button_clear.setDisabled(False)
        self.toolBar.addAction(self.button_clear)

        # Toolbar delete button
        self.button_trash = QAction(QIcon(os.path.join(sys._MEIPASS, 'trash.png')), "Delete", self)
        self.button_trash.setStatusTip("Delete Read Results")
        self.button_trash.triggered.connect(self.trashReadResults)
        self.button_trash.setDisabled(False)
        self.toolBar.addAction(self.button_trash)

        self.toolBar.addSeparator()
        
        # Toolbar platforms button
        self.button_platforms = QAction(QIcon(os.path.join(sys._MEIPASS, 'platforms.png')), "Platforms", self)
        self.button_platforms.setStatusTip("Searching and Platforms")
        self.button_platforms.triggered.connect(self.displayPlatformsDialog)
        self.button_platforms.setDisabled(False)
        self.toolBar.addAction(self.button_platforms)
        # Toolbar Credentials
        self.button_credentials = QAction(QIcon(os.path.join(sys._MEIPASS, 'credentials.png')), "Credentials", self)
        self.button_credentials.setStatusTip("Credentials")
        self.button_credentials.triggered.connect(self.displayAuthenticationSetup)
        self.button_credentials.setDisabled(False)
        self.toolBar.addAction(self.button_credentials)

        # Toolbar Spacer
        toolbarSpacer = ToolBarSpacer()
        self.toolBar.addWidget(toolbarSpacer)

        # Toolbar Settings (align right)
        self.button_settings = QAction(QIcon(os.path.join(sys._MEIPASS, 'settings.png')), "Settings", self)
        self.button_settings.setStatusTip("Settings")
        self.button_settings.triggered.connect(self.displaySettingsDialog)
        self.button_settings.setDisabled(False)
        self.toolBar.addAction(self.button_settings)

        # Setup Status Bar
        self.iconStatusBar = None
        self.updateIconStatusBar(OFFLINE)

        # Table Data
        self.tableWidget = TableWidget()
        self.main.addWidget(self.tableWidget)

        # Check if search on startup is enabled
        if self.settings.searchOnStartup:
            self.start()
     
    def about(self):
        about = AboutDialog(self)
        about.show()

    def displayAuthenticationSetup(self, *args, **kwargs):
        wizard = SetupWizard(self, True)
        wizard.show()

    def updateData(self, d):
        if len(d) > 0:
            self.tableWidget.addData(d)

    def updateIconStatusBar(self, state):
        if self.iconStatusBar is not None:
            self.statusbar.removeWidget(self.iconStatusBar)
        self.iconStatusBar = IconStatusBar(state)
        self.statusbar.addPermanentWidget(self.iconStatusBar)

    def displayPlatformsDialog(self, *args, **kwargs):
        dialog = PlatformsDialog()
        dialog.exec()
    
    def displaySettingsDialog(self, *args, **kwargs):
        dialog = SettingsDialog(parent = self)
        dialog.exec()

    def sendNotification(self, t):
        if self.tray.supportsMessages():
            self.tray.showMessage(t[0], t[1], self.trayIcon)

    def reap(self):
        self.gamefinder.wait()

    def markResultsRead(self, *args, **kwargs):
        self.tableWidget.markResultsRead()

    def trashReadResults(self, *args, **kwargs):
        color = self.tableWidget.getColorFromHex("FFFFFF")
        rowCount = self.tableWidget.rowCount()
        lastRow = -1
        row = 0

        while row < rowCount:
            if lastRow > -1:
                row = lastRow
                lastRow = -1

            item = self.tableWidget.item(row, 0)

            if item is not None:
                background = item.background()
                if background is not None:
                    if background.color().__eq__(color):
                        self.tableWidget.removeRow(row)
                        lastRow = row

            row += 1

        item = self.tableWidget.item(0, 0)
        if item is not None:
            self.tableWidget.scrollToItem(item)

    def start(self, *args, **kwargs):
        if self.button_start.isEnabled():
            self.button_start.setDisabled(True)
            self.button_stop.setDisabled(False)
        self.running = True
        self.updateIconStatusBar(ONLINE)
        self.gamefinder.run()

    def shutdown(self, *args, **kwargs):
        self.running = False
        self.stop()
        app.quit()
        self.reap()

    def isRunning(self):
        return self.running

    def stop(self, *args, **kwargs):
        if self.button_stop.isEnabled():
            self.button_stop.setDisabled(True)
            self.button_start.setDisabled(False)
        self.updateIconStatusBar(OFFLINE)
        self.gamefinder.stop()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, handler)

    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        Info.FROZEN = True

    app = QApplication([])
    app.setQuitOnLastWindowClosed(False)

    if Info.FROZEN:
        appData = os.path.join(os.environ['APPDATA'], Info.APPNAME)
        ebayYaml = os.path.join(appData, 'ebay.yaml')

        if not os.path.exists(appData):
             os.mkdir(appData)

        window = MainWindow()

        if not os.path.exists(os.path.join(os.environ['APPDATA'], Info.APPNAME, 'ebay.yaml')):
            window.show()
            window.activateWindow()
            wizard = SetupWizard(window)
            wizard.show()
        else:
            window.show()
            window.activateWindow()

         # Start QT Application
        app.exec()

        # Wait for threads to exit
        window.reap()