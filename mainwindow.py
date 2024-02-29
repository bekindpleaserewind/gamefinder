# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QMainWindow,
    QMenu, QMenuBar, QScrollArea, QSizePolicy,
    QSplitter, QStatusBar, QToolBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setMinimumSize(QSize(1024, 768))
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionStart = QAction(MainWindow)
        self.actionStart.setObjectName(u"actionStart")
        self.actionStop = QAction(MainWindow)
        self.actionStop.setObjectName(u"actionStop")
        self.actionConfigure = QAction(MainWindow)
        self.actionConfigure.setObjectName(u"actionConfigure")
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionAuthentication = QAction(MainWindow)
        self.actionAuthentication.setObjectName(u"actionAuthentication")
        self.actionPlatforms = QAction(MainWindow)
        self.actionPlatforms.setObjectName(u"actionPlatforms")
        self.actionToolbar = QAction(MainWindow)
        self.actionToolbar.setObjectName(u"actionToolbar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setMaximumSize(QSize(16777215, 16777215))
        self.splitter.setOrientation(Qt.Vertical)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.main = QVBoxLayout(self.verticalLayoutWidget)
        self.main.setObjectName(u"main")
        self.main.setContentsMargins(0, 0, 0, 0)
        self.splitter.addWidget(self.verticalLayoutWidget)
        self.consoleGroupBox = QGroupBox(self.splitter)
        self.consoleGroupBox.setObjectName(u"consoleGroupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.consoleGroupBox.sizePolicy().hasHeightForWidth())
        self.consoleGroupBox.setSizePolicy(sizePolicy)
        self.consoleGroupBox.setMinimumSize(QSize(0, 0))
        self.consoleGroupBox.setMaximumSize(QSize(16777215, 128))
        self.verticalLayout = QVBoxLayout(self.consoleGroupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.consoleLayout = QVBoxLayout()
        self.consoleLayout.setObjectName(u"consoleLayout")
        self.consoleScroll = QScrollArea(self.consoleGroupBox)
        self.consoleScroll.setObjectName(u"consoleScroll")
        self.consoleScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.consoleScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.consoleScroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 965, 71))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.consoleLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.consoleLabel.setObjectName(u"consoleLabel")
        self.consoleLabel.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.consoleLabel.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.verticalLayout_3.addWidget(self.consoleLabel)

        self.consoleScroll.setWidget(self.scrollAreaWidgetContents_2)

        self.consoleLayout.addWidget(self.consoleScroll)


        self.verticalLayout.addLayout(self.consoleLayout)

        self.splitter.addWidget(self.consoleGroupBox)

        self.verticalLayout_2.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuSearch = QMenu(self.menubar)
        self.menuSearch.setObjectName(u"menuSearch")
        self.menuEbay = QMenu(self.menubar)
        self.menuEbay.setObjectName(u"menuEbay")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        self.statusbar.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setIconSize(QSize(32, 32))
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEbay.menuAction())
        self.menubar.addAction(self.menuSearch.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuSearch.addAction(self.actionStart)
        self.menuSearch.addAction(self.actionStop)
        self.menuEbay.addAction(self.actionPlatforms)
        self.menuEbay.addAction(self.actionAuthentication)
        self.menuView.addAction(self.actionToolbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gamefinder", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionStart.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.actionStop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.actionConfigure.setText(QCoreApplication.translate("MainWindow", u"Configure", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionAuthentication.setText(QCoreApplication.translate("MainWindow", u"Authentication", None))
        self.actionPlatforms.setText(QCoreApplication.translate("MainWindow", u"Platforms", None))
        self.actionToolbar.setText(QCoreApplication.translate("MainWindow", u"Toolbar", None))
        self.consoleGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Console", None))
        self.consoleLabel.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuSearch.setTitle(QCoreApplication.translate("MainWindow", u"Search", None))
        self.menuEbay.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

