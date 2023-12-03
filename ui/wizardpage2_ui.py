# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wizardpage2.ui'
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

class Ui_WizardPage2(object):
    def setupUi(self, WizardPage2):
        if not WizardPage2.objectName():
            WizardPage2.setObjectName(u"WizardPage2")
        WizardPage2.resize(629, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WizardPage2.sizePolicy().hasHeightForWidth())
        WizardPage2.setSizePolicy(sizePolicy)
        WizardPage2.setMinimumSize(QSize(0, 0))
        self.gridLayout = QGridLayout(WizardPage2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 20, -1, -1)
        self.lineEditAppid = QLineEdit(WizardPage2)
        self.lineEditAppid.setObjectName(u"lineEditAppid")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEditAppid.sizePolicy().hasHeightForWidth())
        self.lineEditAppid.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.lineEditAppid, 0, 1, 1, 1)

        self.labelCertid = QLabel(WizardPage2)
        self.labelCertid.setObjectName(u"labelCertid")

        self.gridLayout.addWidget(self.labelCertid, 1, 0, 1, 1)

        self.labelToken = QLabel(WizardPage2)
        self.labelToken.setObjectName(u"labelToken")

        self.gridLayout.addWidget(self.labelToken, 3, 0, 1, 1)

        self.lineEditCertid = QLineEdit(WizardPage2)
        self.lineEditCertid.setObjectName(u"lineEditCertid")

        self.gridLayout.addWidget(self.lineEditCertid, 1, 1, 1, 1)

        self.lineEditDevid = QLineEdit(WizardPage2)
        self.lineEditDevid.setObjectName(u"lineEditDevid")

        self.gridLayout.addWidget(self.lineEditDevid, 2, 1, 1, 1)

        self.lineEditToken = QLineEdit(WizardPage2)
        self.lineEditToken.setObjectName(u"lineEditToken")

        self.gridLayout.addWidget(self.lineEditToken, 3, 1, 1, 1)

        self.labelDevid = QLabel(WizardPage2)
        self.labelDevid.setObjectName(u"labelDevid")

        self.gridLayout.addWidget(self.labelDevid, 2, 0, 1, 1)

        self.labelAppid = QLabel(WizardPage2)
        self.labelAppid.setObjectName(u"labelAppid")

        self.gridLayout.addWidget(self.labelAppid, 0, 0, 1, 1)


        self.retranslateUi(WizardPage2)

        QMetaObject.connectSlotsByName(WizardPage2)
    # setupUi

    def retranslateUi(self, WizardPage2):
        WizardPage2.setWindowTitle("")
        WizardPage2.setTitle(QCoreApplication.translate("WizardPage2", u"Production Credentials", None))
        WizardPage2.setSubTitle(QCoreApplication.translate("WizardPage2", u"From here you will configure your Ebay production API credentials.", None))
        self.labelCertid.setText(QCoreApplication.translate("WizardPage2", u"certid", None))
        self.labelToken.setText(QCoreApplication.translate("WizardPage2", u"token", None))
        self.labelDevid.setText(QCoreApplication.translate("WizardPage2", u"devid", None))
        self.labelAppid.setText(QCoreApplication.translate("WizardPage2", u"appid", None))
    # retranslateUi

