# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widgetsaved.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QSizePolicy, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_widgetsaved(object):
    def setupUi(self, widgetsaved):
        if not widgetsaved.objectName():
            widgetsaved.setObjectName(u"widgetsaved")
        widgetsaved.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widgetsaved.sizePolicy().hasHeightForWidth())
        widgetsaved.setSizePolicy(sizePolicy)
        widgetsaved.setWindowOpacity(0.000000000000000)
        self.verticalLayout = QVBoxLayout(widgetsaved)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.body = QTreeWidget(widgetsaved)
        self.body.setObjectName(u"body")
        self.body.header().setVisible(False)

        self.verticalLayout.addWidget(self.body)


        self.retranslateUi(widgetsaved)

        QMetaObject.connectSlotsByName(widgetsaved)
    # setupUi

    def retranslateUi(self, widgetsaved):
        widgetsaved.setWindowTitle(QCoreApplication.translate("widgetsaved", u"Form", None))
        ___qtreewidgetitem = self.body.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("widgetsaved", u"1", None));
    # retranslateUi

