# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_settings.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(623, 360)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titleBarWidget = QWidget(Form)
        self.titleBarWidget.setObjectName(u"titleBarWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleBarWidget.sizePolicy().hasHeightForWidth())
        self.titleBarWidget.setSizePolicy(sizePolicy)
        self.titleBarWidget.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.titleBarWidget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleWidget = QWidget(self.titleBarWidget)
        self.titleWidget.setObjectName(u"titleWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.titleWidget.sizePolicy().hasHeightForWidth())
        self.titleWidget.setSizePolicy(sizePolicy1)
        self.titleWidget.setMinimumSize(QSize(0, 50))
        self.titleWidget.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.titleWidget)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sectionTitle = QLabel(self.titleWidget)
        self.sectionTitle.setObjectName(u"sectionTitle")
        sizePolicy.setHeightForWidth(self.sectionTitle.sizePolicy().hasHeightForWidth())
        self.sectionTitle.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.sectionTitle)


        self.horizontalLayout_3.addWidget(self.titleWidget)

        self.windowControlsWidget = QWidget(self.titleBarWidget)
        self.windowControlsWidget.setObjectName(u"windowControlsWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.windowControlsWidget.sizePolicy().hasHeightForWidth())
        self.windowControlsWidget.setSizePolicy(sizePolicy2)
        self.windowControlsWidget.setMinimumSize(QSize(200, 50))
        self.windowControlsWidget.setMaximumSize(QSize(16777215, 50))
        self.windowControlsWidget.setStyleSheet(u"QPushButton{\n"
"	width: 60px;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.windowControlsWidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.windowControlsWidget)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 0))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeAppBtn.setIcon(icon)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.minimizeAppBtn)

        self.maximizeAppBtn = QPushButton(self.windowControlsWidget)
        self.maximizeAppBtn.setObjectName(u"maximizeAppBtn")
        self.maximizeAppBtn.setMinimumSize(QSize(28, 0))
        self.maximizeAppBtn.setMaximumSize(QSize(28, 28))
        self.maximizeAppBtn.setLayoutDirection(Qt.LeftToRight)
        self.maximizeAppBtn.setStyleSheet(u"pushButton_9{\n"
"	transform: scaleX(-1);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/feather/icons/feather/maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximizeAppBtn.setIcon(icon1)
        self.maximizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.maximizeAppBtn)

        self.closeAppBtn = QPushButton(self.windowControlsWidget)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 0))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setStyleSheet(u"#closeAppBtn{\n"
"	width: 60px;\n"
"	\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/feather/icons/feather/window_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeAppBtn.setIcon(icon2)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.closeAppBtn)


        self.horizontalLayout_3.addWidget(self.windowControlsWidget, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.titleBarWidget)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.themGB = QGroupBox(self.widget)
        self.themGB.setObjectName(u"themGB")
        self.gridLayout = QGridLayout(self.themGB)
        self.gridLayout.setObjectName(u"gridLayout")
        self.themeName = QLabel(self.themGB)
        self.themeName.setObjectName(u"themeName")

        self.gridLayout.addWidget(self.themeName, 0, 0, 1, 1)

        self.themeList = QComboBox(self.themGB)
        self.themeList.setObjectName(u"themeList")

        self.gridLayout.addWidget(self.themeList, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.themGB, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Settings", None))
        self.sectionTitle.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.minimizeAppBtn.setText("")
        self.maximizeAppBtn.setText("")
        self.closeAppBtn.setText("")
        self.themGB.setTitle(QCoreApplication.translate("Form", u"Theme", None))
        self.themeName.setText(QCoreApplication.translate("Form", u"Theme Name", None))
    # retranslateUi

