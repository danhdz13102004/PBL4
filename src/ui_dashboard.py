# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_dashboard.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(725, 498)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.gridLayout_2 = QGridLayout(self.styleSheet)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.app = QWidget(self.styleSheet)
        self.app.setObjectName(u"app")
        self.horizontalLayout_5 = QHBoxLayout(self.app)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.sidebarWidget = QWidget(self.app)
        self.sidebarWidget.setObjectName(u"sidebarWidget")
        self.verticalLayout_4 = QVBoxLayout(self.sidebarWidget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.topSBWidget = QWidget(self.sidebarWidget)
        self.topSBWidget.setObjectName(u"topSBWidget")
        self.topSBWidget.setMinimumSize(QSize(0, 50))
        self.topSBWidget.setMaximumSize(QSize(16777215, 50))
        self.logo = QFrame(self.topSBWidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(0, 0, 61, 51))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.appTitle = QLabel(self.topSBWidget)
        self.appTitle.setObjectName(u"appTitle")
        self.appTitle.setGeometry(QRect(72, 9, 47, 15))
        self.appDescription = QLabel(self.topSBWidget)
        self.appDescription.setObjectName(u"appDescription")
        self.appDescription.setGeometry(QRect(72, 28, 80, 16))

        self.verticalLayout_4.addWidget(self.topSBWidget)

        self.mainSBWidget = QWidget(self.sidebarWidget)
        self.mainSBWidget.setObjectName(u"mainSBWidget")
        self.mainSBWidget.setMinimumSize(QSize(60, 0))
        self.mainSBWidget.setMaximumSize(QSize(60, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.mainSBWidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 10, 5, 0)
        self.topMenu = QWidget(self.mainSBWidget)
        self.topMenu.setObjectName(u"topMenu")
        self.verticalLayout_2 = QVBoxLayout(self.topMenu)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.manageClientsBtn = QPushButton(self.topMenu)
        self.manageClientsBtn.setObjectName(u"manageClientsBtn")
        self.manageClientsBtn.setMinimumSize(QSize(0, 45))
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.manageClientsBtn.setIcon(icon)

        self.verticalLayout_2.addWidget(self.manageClientsBtn)

        self.showSystemInfoBtn = QPushButton(self.topMenu)
        self.showSystemInfoBtn.setObjectName(u"showSystemInfoBtn")
        self.showSystemInfoBtn.setMinimumSize(QSize(0, 45))
        icon1 = QIcon()
        icon1.addFile(u":/material_design/icons/material_design/computer.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.showSystemInfoBtn.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.showSystemInfoBtn)

        self.viewLocationBtn = QPushButton(self.topMenu)
        self.viewLocationBtn.setObjectName(u"viewLocationBtn")
        self.viewLocationBtn.setMinimumSize(QSize(0, 45))
        icon2 = QIcon()
        icon2.addFile(u":/feather/icons/feather/map.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.viewLocationBtn.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.viewLocationBtn)


        self.verticalLayout_3.addWidget(self.topMenu, 0, Qt.AlignLeft|Qt.AlignTop)

        self.bottomMenu = QWidget(self.mainSBWidget)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.verticalLayout = QVBoxLayout(self.bottomMenu)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 5)
        self.settingsBtn = QPushButton(self.bottomMenu)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setMinimumSize(QSize(0, 45))
        icon3 = QIcon()
        icon3.addFile(u":/feather/icons/feather/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsBtn.setIcon(icon3)

        self.verticalLayout.addWidget(self.settingsBtn)

        self.helpBtn = QPushButton(self.bottomMenu)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setMinimumSize(QSize(0, 45))
        icon4 = QIcon()
        icon4.addFile(u":/feather/icons/feather/help-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.helpBtn.setIcon(icon4)

        self.verticalLayout.addWidget(self.helpBtn)


        self.verticalLayout_3.addWidget(self.bottomMenu, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.verticalLayout_4.addWidget(self.mainSBWidget, 0, Qt.AlignLeft)


        self.horizontalLayout_5.addWidget(self.sidebarWidget)

        self.contentWidget = QWidget(self.app)
        self.contentWidget.setObjectName(u"contentWidget")
        self.verticalLayout_6 = QVBoxLayout(self.contentWidget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.titleBarWidget = QWidget(self.contentWidget)
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
        self.horizontalLayout_2.setContentsMargins(10, 0, 0, 0)
        self.toggleSidebarBtn = QPushButton(self.titleWidget)
        self.toggleSidebarBtn.setObjectName(u"toggleSidebarBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.toggleSidebarBtn.sizePolicy().hasHeightForWidth())
        self.toggleSidebarBtn.setSizePolicy(sizePolicy2)
        self.toggleSidebarBtn.setMinimumSize(QSize(28, 28))
        self.toggleSidebarBtn.setMaximumSize(QSize(28, 28))
        icon5 = QIcon()
        icon5.addFile(u":/feather/icons/feather/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toggleSidebarBtn.setIcon(icon5)
        self.toggleSidebarBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.toggleSidebarBtn)

        self.sectionTitle = QLabel(self.titleWidget)
        self.sectionTitle.setObjectName(u"sectionTitle")
        sizePolicy.setHeightForWidth(self.sectionTitle.sizePolicy().hasHeightForWidth())
        self.sectionTitle.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.sectionTitle)


        self.horizontalLayout_3.addWidget(self.titleWidget)

        self.windowControlsWidget = QWidget(self.titleBarWidget)
        self.windowControlsWidget.setObjectName(u"windowControlsWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.windowControlsWidget.sizePolicy().hasHeightForWidth())
        self.windowControlsWidget.setSizePolicy(sizePolicy3)
        self.windowControlsWidget.setMinimumSize(QSize(200, 50))
        self.windowControlsWidget.setMaximumSize(QSize(16777215, 50))
        self.windowControlsWidget.setStyleSheet(u"QPushButton{\n"
"	width: 60px;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.windowControlsWidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.settingsAppBtn = QPushButton(self.windowControlsWidget)
        self.settingsAppBtn.setObjectName(u"settingsAppBtn")
        self.settingsAppBtn.setMinimumSize(QSize(28, 0))
        self.settingsAppBtn.setMaximumSize(QSize(28, 28))
        self.settingsAppBtn.setStyleSheet(u"")
        self.settingsAppBtn.setIcon(icon3)
        self.settingsAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.settingsAppBtn)

        self.minimizeAppBtn = QPushButton(self.windowControlsWidget)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 0))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        icon6 = QIcon()
        icon6.addFile(u":/feather/icons/feather/minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeAppBtn.setIcon(icon6)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.minimizeAppBtn)

        self.restoreAppBtn = QPushButton(self.windowControlsWidget)
        self.restoreAppBtn.setObjectName(u"restoreAppBtn")
        self.restoreAppBtn.setMinimumSize(QSize(28, 0))
        self.restoreAppBtn.setMaximumSize(QSize(28, 28))
        self.restoreAppBtn.setLayoutDirection(Qt.LeftToRight)
        self.restoreAppBtn.setStyleSheet(u"pushButton_9{\n"
"	transform: scaleX(-1);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/material_design/icons/material_design/zoom_out_map.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restoreAppBtn.setIcon(icon7)
        self.restoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.restoreAppBtn)

        self.closeAppBtn = QPushButton(self.windowControlsWidget)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 0))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setStyleSheet(u"#closeAppBtn{\n"
"	width: 60px;\n"
"	\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/feather/icons/feather/window_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeAppBtn.setIcon(icon8)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.closeAppBtn)


        self.horizontalLayout_3.addWidget(self.windowControlsWidget)


        self.verticalLayout_6.addWidget(self.titleBarWidget)

        self.mainContentWidget = QWidget(self.contentWidget)
        self.mainContentWidget.setObjectName(u"mainContentWidget")
        sizePolicy1.setHeightForWidth(self.mainContentWidget.sizePolicy().hasHeightForWidth())
        self.mainContentWidget.setSizePolicy(sizePolicy1)
        self.verticalLayout_5 = QVBoxLayout(self.mainContentWidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 5)
        self.stackedWidget = QStackedWidget(self.mainContentWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.manageClientsPage = QWidget()
        self.manageClientsPage.setObjectName(u"manageClientsPage")
        self.verticalLayout_8 = QVBoxLayout(self.manageClientsPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.pageTitle = QLabel(self.manageClientsPage)
        self.pageTitle.setObjectName(u"pageTitle")

        self.verticalLayout_8.addWidget(self.pageTitle)

        self.tableWidget = QTableWidget(self.manageClientsPage)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.horizontalHeader().setMinimumSectionSize(150)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_8.addWidget(self.tableWidget)

        self.stackedWidget.addWidget(self.manageClientsPage)
        self.showSystemInfoPage = QWidget()
        self.showSystemInfoPage.setObjectName(u"showSystemInfoPage")
        self.label_3 = QLabel(self.showSystemInfoPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(26, 10, 241, 31))
        self.stackedWidget.addWidget(self.showSystemInfoPage)
        self.viewLocationPage = QWidget()
        self.viewLocationPage.setObjectName(u"viewLocationPage")
        self.stackedWidget.addWidget(self.viewLocationPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.formLayout = QFormLayout(self.settingsPage)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(40)
        self.formLayout.setContentsMargins(100, -1, 150, -1)
        self.label = QLabel(self.settingsPage)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.themeList = QComboBox(self.settingsPage)
        self.themeList.setObjectName(u"themeList")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.themeList)

        self.stackedWidget.addWidget(self.settingsPage)
        self.helpPage = QWidget()
        self.helpPage.setObjectName(u"helpPage")
        self.stackedWidget.addWidget(self.helpPage)

        self.verticalLayout_5.addWidget(self.stackedWidget)

        self.creditWidget = QWidget(self.mainContentWidget)
        self.creditWidget.setObjectName(u"creditWidget")
        self.creditWidget.setMinimumSize(QSize(0, 20))
        self.creditWidget.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_6 = QHBoxLayout(self.creditWidget)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.credit = QFrame(self.creditWidget)
        self.credit.setObjectName(u"credit")
        self.credit.setMinimumSize(QSize(0, 20))
        self.credit.setMaximumSize(QSize(16777215, 20))
        self.credit.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_4 = QHBoxLayout(self.credit)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 0, 10, 0)
        self.creditLabel = QLabel(self.credit)
        self.creditLabel.setObjectName(u"creditLabel")
        sizePolicy1.setHeightForWidth(self.creditLabel.sizePolicy().hasHeightForWidth())
        self.creditLabel.setSizePolicy(sizePolicy1)
        self.creditLabel.setMinimumSize(QSize(400, 20))

        self.horizontalLayout_4.addWidget(self.creditLabel)

        self.widget = QWidget(self.credit)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 20))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.nameOfTheme = QLabel(self.widget)
        self.nameOfTheme.setObjectName(u"nameOfTheme")
        self.nameOfTheme.setMinimumSize(QSize(0, 20))

        self.gridLayout.addWidget(self.nameOfTheme, 0, 0, 1, 1, Qt.AlignRight)

        self.themeProgress = QProgressBar(self.widget)
        self.themeProgress.setObjectName(u"themeProgress")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.themeProgress.sizePolicy().hasHeightForWidth())
        self.themeProgress.setSizePolicy(sizePolicy4)
        self.themeProgress.setMinimumSize(QSize(0, 10))
        self.themeProgress.setMaximumSize(QSize(150, 10))
        self.themeProgress.setValue(24)
        self.themeProgress.setTextVisible(False)

        self.gridLayout.addWidget(self.themeProgress, 0, 1, 1, 1, Qt.AlignVCenter)


        self.horizontalLayout_4.addWidget(self.widget)


        self.horizontalLayout_6.addWidget(self.credit)

        self.sizeGrip = QFrame(self.creditWidget)
        self.sizeGrip.setObjectName(u"sizeGrip")
        sizePolicy3.setHeightForWidth(self.sizeGrip.sizePolicy().hasHeightForWidth())
        self.sizeGrip.setSizePolicy(sizePolicy3)
        self.sizeGrip.setMinimumSize(QSize(20, 20))
        self.sizeGrip.setMaximumSize(QSize(20, 20))
        self.sizeGrip.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_6.addWidget(self.sizeGrip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_5.addWidget(self.creditWidget)


        self.verticalLayout_6.addWidget(self.mainContentWidget)


        self.horizontalLayout_5.addWidget(self.contentWidget)


        self.gridLayout_2.addWidget(self.app, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.appTitle.setText(QCoreApplication.translate("MainWindow", u"Server", None))
        self.appDescription.setText(QCoreApplication.translate("MainWindow", u"Botnet Master", None))
        self.manageClientsBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.showSystemInfoBtn.setText(QCoreApplication.translate("MainWindow", u"System", None))
        self.viewLocationBtn.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.toggleSidebarBtn.setText("")
        self.sectionTitle.setText(QCoreApplication.translate("MainWindow", u"Botnet Client Management", None))
        self.settingsAppBtn.setText("")
        self.minimizeAppBtn.setText("")
        self.restoreAppBtn.setText("")
        self.closeAppBtn.setText("")
        self.pageTitle.setText(QCoreApplication.translate("MainWindow", u"Danh s\u00e1ch client k\u1ebft n\u1ed1i", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"IP", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"User@PC", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Country", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Show system Page", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Select Theme", None))
        self.creditLabel.setText(QCoreApplication.translate("MainWindow", u"PBL4", None))
        self.nameOfTheme.setText(QCoreApplication.translate("MainWindow", u"Theme", None))
    # retranslateUi

