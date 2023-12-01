# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wizardpage1.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget, QWizardPage)

class Ui_WizardPage1(object):
    def setupUi(self, WizardPage1):
        if not WizardPage1.objectName():
            WizardPage1.setObjectName(u"WizardPage1")
        WizardPage1.resize(860, 524)
        self.verticalLayout = QVBoxLayout(WizardPage1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(WizardPage1)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.MarkdownText)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)


        self.retranslateUi(WizardPage1)

        QMetaObject.connectSlotsByName(WizardPage1)
    # setupUi

    def retranslateUi(self, WizardPage1):
        WizardPage1.setWindowTitle(QCoreApplication.translate("WizardPage1", u"WizardPage", None))
        WizardPage1.setTitle(QCoreApplication.translate("WizardPage1", u"Ebay Game Monitor", None))
        WizardPage1.setSubTitle("")
        self.label.setText(QCoreApplication.translate("WizardPage1", u"Welcome to the configuration wizard for Ebay Game Monitor!\n"
"\n"
"\n"
"This wizard will guide you through the process of configuring your development credentials for both the sandbox and production APIs.  Once complete, your application will have full access to monitor different game categories on ebay for anything you'd like to search for.   Remember to make sure you've setup your developer account at <a href=\"https://developer.ebay.com\">https://developer.ebay.com</a> and registered a new application before continuing!", None))
    # retranslateUi

