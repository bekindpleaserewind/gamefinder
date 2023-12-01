# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'platforms.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFormLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Platforms(object):
    def setupUi(self, Platforms):
        if not Platforms.objectName():
            Platforms.setObjectName(u"Platforms")
        Platforms.resize(800, 600)
        self.verticalLayout_2 = QVBoxLayout(Platforms)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.categoryLabel = QLabel(Platforms)
        self.categoryLabel.setObjectName(u"categoryLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.categoryLabel)

        self.category = QComboBox(Platforms)
        self.category.setObjectName(u"category")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.category.sizePolicy().hasHeightForWidth())
        self.category.setSizePolicy(sizePolicy)
        self.category.setMinimumSize(QSize(192, 0))
        self.category.setEditable(False)
        self.category.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.category)

        self.conditionsLabel = QLabel(Platforms)
        self.conditionsLabel.setObjectName(u"conditionsLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.conditionsLabel)

        self.conditions = QComboBox(Platforms)
        self.conditions.setObjectName(u"conditions")
        sizePolicy.setHeightForWidth(self.conditions.sizePolicy().hasHeightForWidth())
        self.conditions.setSizePolicy(sizePolicy)
        self.conditions.setMinimumSize(QSize(192, 0))
        self.conditions.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.conditions)

        self.locationLabel = QLabel(Platforms)
        self.locationLabel.setObjectName(u"locationLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.locationLabel)

        self.locations = QComboBox(Platforms)
        self.locations.setObjectName(u"locations")
        sizePolicy.setHeightForWidth(self.locations.sizePolicy().hasHeightForWidth())
        self.locations.setSizePolicy(sizePolicy)
        self.locations.setMinimumSize(QSize(192, 0))
        self.locations.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.locations)

        self.models = QComboBox(Platforms)
        self.models.setObjectName(u"models")
        sizePolicy.setHeightForWidth(self.models.sizePolicy().hasHeightForWidth())
        self.models.setSizePolicy(sizePolicy)
        self.models.setMinimumSize(QSize(192, 0))
        self.models.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.models)

        self.platformsLabel = QLabel(Platforms)
        self.platformsLabel.setObjectName(u"platformsLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.platformsLabel)

        self.platforms = QComboBox(Platforms)
        self.platforms.setObjectName(u"platforms")
        sizePolicy.setHeightForWidth(self.platforms.sizePolicy().hasHeightForWidth())
        self.platforms.setSizePolicy(sizePolicy)
        self.platforms.setMinimumSize(QSize(192, 0))
        self.platforms.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.platforms)

        self.modelsLabel = QLabel(Platforms)
        self.modelsLabel.setObjectName(u"modelsLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.modelsLabel)


        self.verticalLayout.addLayout(self.formLayout)

        self.inputSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.inputSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.create = QPushButton(Platforms)
        self.create.setObjectName(u"create")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.create.sizePolicy().hasHeightForWidth())
        self.create.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.create)

        self.remove = QPushButton(Platforms)
        self.remove.setObjectName(u"remove")
        sizePolicy1.setHeightForWidth(self.remove.sizePolicy().hasHeightForWidth())
        self.remove.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.remove)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.rightVLayout = QVBoxLayout()
        self.rightVLayout.setObjectName(u"rightVLayout")
        self.search = QLineEdit(Platforms)
        self.search.setObjectName(u"search")

        self.rightVLayout.addWidget(self.search)

        self.root = QTreeWidget(Platforms)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(1, u"2");
        self.root.setHeaderItem(__qtreewidgetitem)
        self.root.setObjectName(u"root")
        self.root.setWordWrap(True)
        self.root.setColumnCount(2)
        self.root.header().setVisible(False)
        self.root.header().setCascadingSectionResizes(True)
        self.root.header().setMinimumSectionSize(100)
        self.root.header().setDefaultSectionSize(150)

        self.rightVLayout.addWidget(self.root)


        self.horizontalLayout_2.addLayout(self.rightVLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.buttonBox = QDialogButtonBox(Platforms)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(Platforms)
        self.buttonBox.accepted.connect(Platforms.accept)
        self.buttonBox.rejected.connect(Platforms.reject)

        QMetaObject.connectSlotsByName(Platforms)
    # setupUi

    def retranslateUi(self, Platforms):
        Platforms.setWindowTitle(QCoreApplication.translate("Platforms", u"Platforms and Searches", None))
        self.categoryLabel.setText(QCoreApplication.translate("Platforms", u"Category", None))
        self.conditionsLabel.setText(QCoreApplication.translate("Platforms", u"Conditions", None))
        self.locationLabel.setText(QCoreApplication.translate("Platforms", u"Location", None))
        self.platformsLabel.setText(QCoreApplication.translate("Platforms", u"Platforms", None))
        self.modelsLabel.setText(QCoreApplication.translate("Platforms", u"Models", None))
        self.create.setText(QCoreApplication.translate("Platforms", u"Create", None))
        self.remove.setText(QCoreApplication.translate("Platforms", u"Remove", None))
        self.search.setPlaceholderText(QCoreApplication.translate("Platforms", u"Enter Search", None))
        ___qtreewidgetitem = self.root.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Platforms", u"Configuration", None));
    # retranslateUi

