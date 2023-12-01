# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wizardpage3.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QSizePolicy, QWidget, QWizardPage)

class Ui_WizardPage3(object):
    def setupUi(self, WizardPage3):
        if not WizardPage3.objectName():
            WizardPage3.setObjectName(u"WizardPage3")
        WizardPage3.resize(400, 300)
        self.gridLayout = QGridLayout(WizardPage3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 20, -1, -1)
        self.lineEditAppid = QLineEdit(WizardPage3)
        self.lineEditAppid.setObjectName(u"lineEditAppid")

        self.gridLayout.addWidget(self.lineEditAppid, 0, 1, 1, 1)

        self.labelCertid = QLabel(WizardPage3)
        self.labelCertid.setObjectName(u"labelCertid")

        self.gridLayout.addWidget(self.labelCertid, 1, 0, 1, 1)

        self.labelToken = QLabel(WizardPage3)
        self.labelToken.setObjectName(u"labelToken")

        self.gridLayout.addWidget(self.labelToken, 3, 0, 1, 1)

        self.lineEditCertid = QLineEdit(WizardPage3)
        self.lineEditCertid.setObjectName(u"lineEditCertid")

        self.gridLayout.addWidget(self.lineEditCertid, 1, 1, 1, 1)

        self.lineEditDevid = QLineEdit(WizardPage3)
        self.lineEditDevid.setObjectName(u"lineEditDevid")

        self.gridLayout.addWidget(self.lineEditDevid, 2, 1, 1, 1)

        self.lineEditToken = QLineEdit(WizardPage3)
        self.lineEditToken.setObjectName(u"lineEditToken")

        self.gridLayout.addWidget(self.lineEditToken, 3, 1, 1, 1)

        self.labelDevid = QLabel(WizardPage3)
        self.labelDevid.setObjectName(u"labelDevid")

        self.gridLayout.addWidget(self.labelDevid, 2, 0, 1, 1)

        self.labelAppid = QLabel(WizardPage3)
        self.labelAppid.setObjectName(u"labelAppid")

        self.gridLayout.addWidget(self.labelAppid, 0, 0, 1, 1)


        self.retranslateUi(WizardPage3)

        QMetaObject.connectSlotsByName(WizardPage3)
    # setupUi

    def retranslateUi(self, WizardPage3):
        WizardPage3.setWindowTitle("")
        WizardPage3.setTitle(QCoreApplication.translate("WizardPage3", u"Production Credentials", None))
        WizardPage3.setSubTitle(QCoreApplication.translate("WizardPage3", u"From here you will configure your Ebay production API credentials.", None))
        self.labelCertid.setText(QCoreApplication.translate("WizardPage3", u"certid", None))
        self.labelToken.setText(QCoreApplication.translate("WizardPage3", u"token", None))
        self.labelDevid.setText(QCoreApplication.translate("WizardPage3", u"devid", None))
        self.labelAppid.setText(QCoreApplication.translate("WizardPage3", u"appid", None))
    # retranslateUi

