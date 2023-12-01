# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(Settings)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ebayGroupBox = QGroupBox(Settings)
        self.ebayGroupBox.setObjectName(u"ebayGroupBox")
        self.formLayout_3 = QFormLayout(self.ebayGroupBox)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.apiCallsPerDayLabel = QLabel(self.ebayGroupBox)
        self.apiCallsPerDayLabel.setObjectName(u"apiCallsPerDayLabel")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.apiCallsPerDayLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.apiCallsPerDay = QLineEdit(self.ebayGroupBox)
        self.apiCallsPerDay.setObjectName(u"apiCallsPerDay")

        self.horizontalLayout_2.addWidget(self.apiCallsPerDay)

        self.horizontalSpacer_2 = QSpacerItem(120, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.formLayout_3.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.automaticIntervalsLabel = QLabel(self.ebayGroupBox)
        self.automaticIntervalsLabel.setObjectName(u"automaticIntervalsLabel")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.automaticIntervalsLabel)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.enabledRadioButton = QRadioButton(self.ebayGroupBox)
        self.enabledRadioButton.setObjectName(u"enabledRadioButton")

        self.verticalLayout.addWidget(self.enabledRadioButton)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.disabledRadioButton = QRadioButton(self.ebayGroupBox)
        self.disabledRadioButton.setObjectName(u"disabledRadioButton")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.disabledRadioButton)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.automaticIntervalMinutes = QLineEdit(self.ebayGroupBox)
        self.automaticIntervalMinutes.setObjectName(u"automaticIntervalMinutes")
        self.automaticIntervalMinutes.setEnabled(True)

        self.horizontalLayout.addWidget(self.automaticIntervalMinutes)

        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout)


        self.verticalLayout.addLayout(self.formLayout)


        self.formLayout_3.setLayout(1, QFormLayout.FieldRole, self.verticalLayout)


        self.verticalLayout_2.addWidget(self.ebayGroupBox)

        self.systemGroupBox = QGroupBox(Settings)
        self.systemGroupBox.setObjectName(u"systemGroupBox")
        self.formLayout_2 = QFormLayout(self.systemGroupBox)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label = QLabel(self.systemGroupBox)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.searchOnStartupOn = QRadioButton(self.systemGroupBox)
        self.searchOnStartupOn.setObjectName(u"searchOnStartupOn")

        self.horizontalLayout_3.addWidget(self.searchOnStartupOn)

        self.searchOnStartupOff = QRadioButton(self.systemGroupBox)
        self.searchOnStartupOff.setObjectName(u"searchOnStartupOff")

        self.horizontalLayout_3.addWidget(self.searchOnStartupOff)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.formLayout_2.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.label_2 = QLabel(self.systemGroupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.enableAudioNotificationOn = QRadioButton(self.systemGroupBox)
        self.enableAudioNotificationOn.setObjectName(u"enableAudioNotificationOn")

        self.horizontalLayout_4.addWidget(self.enableAudioNotificationOn)

        self.enableAudioNotificationOff = QRadioButton(self.systemGroupBox)
        self.enableAudioNotificationOff.setObjectName(u"enableAudioNotificationOff")

        self.horizontalLayout_4.addWidget(self.enableAudioNotificationOff)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.formLayout_2.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.label_3 = QLabel(self.systemGroupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.enableDesktopNotificationOn = QRadioButton(self.systemGroupBox)
        self.enableDesktopNotificationOn.setObjectName(u"enableDesktopNotificationOn")

        self.horizontalLayout_5.addWidget(self.enableDesktopNotificationOn)

        self.enableDesktopNotificationOff = QRadioButton(self.systemGroupBox)
        self.enableDesktopNotificationOff.setObjectName(u"enableDesktopNotificationOff")

        self.horizontalLayout_5.addWidget(self.enableDesktopNotificationOff)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.formLayout_2.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_5)


        self.verticalLayout_2.addWidget(self.systemGroupBox)

        self.buttonBox = QDialogButtonBox(Settings)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(Settings)
        self.buttonBox.accepted.connect(Settings.accept)
        self.buttonBox.rejected.connect(Settings.reject)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Settings", None))
        self.ebayGroupBox.setTitle(QCoreApplication.translate("Settings", u"Ebay", None))
        self.apiCallsPerDayLabel.setText(QCoreApplication.translate("Settings", u"API Calls Per Day", None))
        self.automaticIntervalsLabel.setText(QCoreApplication.translate("Settings", u"Automatic Intervals", None))
        self.enabledRadioButton.setText(QCoreApplication.translate("Settings", u"Enabled", None))
        self.disabledRadioButton.setText(QCoreApplication.translate("Settings", u"Disabled", None))
        self.automaticIntervalMinutes.setPlaceholderText(QCoreApplication.translate("Settings", u"Minutes", None))
        self.systemGroupBox.setTitle(QCoreApplication.translate("Settings", u"System", None))
        self.label.setText(QCoreApplication.translate("Settings", u"Search on Startup", None))
        self.searchOnStartupOn.setText(QCoreApplication.translate("Settings", u"On", None))
        self.searchOnStartupOff.setText(QCoreApplication.translate("Settings", u"Off", None))
        self.label_2.setText(QCoreApplication.translate("Settings", u"Enable Audio Notifications", None))
        self.enableAudioNotificationOn.setText(QCoreApplication.translate("Settings", u"On", None))
        self.enableAudioNotificationOff.setText(QCoreApplication.translate("Settings", u"Off", None))
        self.label_3.setText(QCoreApplication.translate("Settings", u"Enable Desktop Notification", None))
        self.enableDesktopNotificationOn.setText(QCoreApplication.translate("Settings", u"On", None))
        self.enableDesktopNotificationOff.setText(QCoreApplication.translate("Settings", u"Off", None))
    # retranslateUi

