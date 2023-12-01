# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widgetmin.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QWidget)

class Ui_widgetmin(object):
    def setupUi(self, widgetmin):
        if not widgetmin.objectName():
            widgetmin.setObjectName(u"widgetmin")
        widgetmin.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widgetmin.sizePolicy().hasHeightForWidth())
        widgetmin.setSizePolicy(sizePolicy)
        widgetmin.setWindowOpacity(0.000000000000000)

        self.retranslateUi(widgetmin)

        QMetaObject.connectSlotsByName(widgetmin)
    # setupUi

    def retranslateUi(self, widgetmin):
        widgetmin.setWindowTitle(QCoreApplication.translate("widgetmin", u"Form", None))
    # retranslateUi

