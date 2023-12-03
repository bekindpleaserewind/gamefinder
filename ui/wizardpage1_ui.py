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
        WizardPage1.resize(451, 283)
        WizardPage1.setMinimumSize(QSize(450, 0))
        self.verticalLayout = QVBoxLayout(WizardPage1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(WizardPage1)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setTextFormat(Qt.MarkdownText)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.label)


        self.retranslateUi(WizardPage1)

        QMetaObject.connectSlotsByName(WizardPage1)
    # setupUi

    def retranslateUi(self, WizardPage1):
        WizardPage1.setWindowTitle(QCoreApplication.translate("WizardPage1", u"WizardPage", None))
        WizardPage1.setTitle(QCoreApplication.translate("WizardPage1", u"Gamefinder", None))
        WizardPage1.setSubTitle("")
        self.label.setText(QCoreApplication.translate("WizardPage1", u"<html><head/><body><p>Welcome to the Ebay developer credential configuration wizard!</p><p>This wizard will guide you through the process of configuring your development credentials for the Ebay production APIs. Once complete, your application will have full access to monitor different game categories on Ebay for anything you'd like to search for. Remember to make sure you have setup your developer account at <br/><a href=\"https://developer.ebay.com\"><span style=\" text-decoration: underline; color:#0000ff;\">https://developer.ebay.com</span></a> and registered a new application before continuing!</p><p>See <a href=\"https://github.com/bekindpleaserewind/gamefinder/blob/main/README.md\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/bekindpleaserewind/gamefinder/blob/main/README.md</span></a> for how to register Ebay developer credentials and setup an application for use with Gamefinder.</p></body></html>", None))
    # retranslateUi

