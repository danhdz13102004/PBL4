from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from Custom_Widgets.QCustomTipOverlay import QCustomTipOverlay
from Custom_Widgets.QCustomLoadingIndicators import QCustom3CirclesLoader

from PySide6.QtCore import QSettings, QTimer, Qt, QObject
from PySide6.QtGui import QFontDatabase, QFont, QIcon, QPalette, QColor, QFontMetrics, QFontMetricsF, QPainter, QPen, QTextDocument, QTextCursor, QTextDocumentFragment, QTextFormat, QTextOption, QTextCharFormat, QTextCursor
from PySide6.QtWidgets import QGraphicsDropShadowEffect

import os, traceback

from .utils_window import Window_Utils
from .utils_sidebar import Sidebar_Utils
from .ui_dashboard import Ui_MainWindow

class GUI_Functions(QObject):
    # Constructor
    def __init__(self, MainWindow):
        super().__init__()
        self.config = None
        self.main: MainWindow = MainWindow                         ## Store MainWindow instance, to handle window events
        self.ui: Ui_MainWindow = MainWindow.ui                     ## Store Ui instance, to handle widget events
        self.window_utils = Window_Utils(MainWindow, self.config)  ## Initialize window utils
        self.sidebar_utils = Sidebar_Utils(MainWindow)             ## Initialize sidebar utils        
        self.ui.manageClientsBtn.setProperty("active", True)
        self.ui.stackedWidget.setCurrentIndex(0)
        
        ## APPLY OTHER CUSTOM TO QMAINWINDOW
        self.window_utils.config_window()

        ## Load sidebar state
        self.sidebar_utils.load_sidebar_state()

        ## Connect sidebar toggle button - 'toggleSidebarBtn'
        self.ui.toggleSidebarBtn.clicked.connect(self.sidebar_utils.toggle_sidebar)

        ## Initialize App Theme
        self.initializeAppTheme()
        
        ## Apply custom font
        self.applyCustomFont()
    
        ## Store settings window reference
        self.settings_window = None
        
        ## List button and page in stacked widget
        self.buttons = {
            self.ui.manageClientsBtn: 0,
            self.ui.showSystemInfoBtn: 1,
            self.ui.viewLocationBtn: 2,
            self.ui.settingsBtn: 3,
            self.ui.helpBtn: 4
        }
        
        ## Setup button style and connect clicked event to stacked widget
        self.setup_button()
    
    ## Initialize App Theme
    def initializeAppTheme(self):
        settings = QSettings()
        current_theme = settings.value("THEME")
        # print(f"Current theme: current_theme")
        
        ## Add theme to theme theme list - 'themeList'
        self.loadThemeList(current_theme)
        
        ## Connect theme change signal to change app theme
        self.ui.themeList.currentIndexChanged.connect(self.changeAppTheme)

    def loadThemeList(self, current_theme):
        self.ui.themeList.clear()
        theme_count = -1
        current_theme = QSettings().value("THEME")

        added_themes = set()

        for theme in self.ui.themes:
            if theme not in added_themes:
                self.ui.themeList.addItem(theme.name, theme.name)
                added_themes.add(theme)

                if theme.defaultTheme or theme.name == current_theme:
                    self.ui.themeList.setCurrentIndex(theme_count)

    def changeAppTheme(self):
        settings = QSettings()
        current_theme = settings.value("THEME")
        selected_theme = self.ui.themeList.currentData()

        if current_theme != selected_theme:
            settings.setValue("THEME", selected_theme)
            new_theme = next((theme for theme in self.ui.themes if theme.name == selected_theme), None)
            if new_theme:
                # Get the icon color from the new theme
                settings = QSettings()
                icon_color = settings.value("Icons-color")
                self.updateIconColors(icon_color)

            QAppSettings.updateAppSettings(self.main, generateIcons=True, reloadJson=True)

    def updateIconColors(self, color):
        if not color:
            return

        # Convert color to QColor if it's a string
        if isinstance(color, str):
            color = QColor(color)

        # List of all buttons that need icon color updates
        buttons_to_update = [
            self.ui.settingsBtn,
            self.ui.helpBtn,
            self.ui.settingsAppBtn,
            self.ui.minimizeAppBtn,
            self.ui.restoreAppBtn,
            self.ui.closeAppBtn,
            self.ui.manageClientsBtn,
            self.ui.showSystemInfoBtn,
            self.ui.viewLocationBtn,
            self.ui.toggleSidebarBtn
        ]

        for button in buttons_to_update:
            if button and hasattr(button, 'icon') and button.icon():
                icon = button.icon()
                sizes = icon.availableSizes()

                if sizes:
                    # Create a new pixmap for each size
                    for size in sizes:
                        original_pixmap = icon.pixmap(size)
                        new_pixmap = original_pixmap.copy()

                        # Create painter
                        painter = QPainter(new_pixmap)
                        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
                        painter.fillRect(new_pixmap.rect(), color)
                        painter.end()

                        # Create new icon with modified pixmap
                        new_icon = QIcon(new_pixmap)
                        button.setIcon(new_icon)

        # Also update any custom widgets that might have icons
        custom_widgets = [
            self.ui.titleWidget,
            self.ui.windowControlsWidget,
            self.ui.bottomMenu,
            self.ui.topMenu
        ]

        for widget in custom_widgets:
            if hasattr(widget, 'updateIconColor'):
                widget.updateIconColor(color)

    def applyCustomFont(self):
        font_id = QFontDatabase.addApplicationFont(os.path.abspath("fonts/google-sans-cufonfonts/ProductSans-Regular.ttf"))
        
        if font_id == -1:
            print(f"Failed to load custom font. Check font file path")
            return
        
        font_family = QFontDatabase.applicationFontFamilies(font_id)
        
        if font_family:
            print(f"Available font families: {font_family}")
            custom_font = QFont(font_family[0])
        else:
            print(f"Font family not found. Falling back to default")
            custom_font = QFont("Sans Serif")

        ## Apply font to MainWindow
        self.main.setFont(custom_font)
        self.main.setStyleSheet(f"font-family: {font_family[0]};")
        print("Font custom is set")
            
    def setup_button(self):
        for button in self.buttons.keys():
            button.setCursor(Qt.PointingHandCursor)
            button.clicked.connect(self.handle_button_click)
            button.setProperty("active", False)
            
    def handle_button_click(self):
        button = self.sender()
        
        for btn in self.buttons.keys():
            btn.setProperty("active", False)
            btn.style().unpolish(btn)   ## Delete style
            btn.style().polish(btn)
        
        button.setProperty("active", True)
        button.style().unpolish(button)
        button.style().polish(button)

        # Chuyển trang trong stackedWidget
        self.ui.stackedWidget.setCurrentIndex(self.buttons[button])    

    