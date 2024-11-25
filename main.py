########################################################################
## IMPORTS

########################################################################
import sys
from PySide6.QtCore import QPoint, Qt
from PySide6.QtWidgets import QMenu
from lxml.html.builder import SELECT
from src.server_handler import Server_Handler
########################################################################
## IMPORT GUI FILE
########################################################################
from src.ui_dashboard import Ui_MainWindow

########################################################################
## IMPORT CUSTOM WIDGETS
########################################################################
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from PySide6.QtWidgets import QApplication

########################################################################
## IMPORT APP FUNCTIONS AND EVENTS
########################################################################
from src.functions_dashboard import GUI_Functions
from src.functions_handler_dashboard import Server_Functions

########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        ########################################################################
        ## APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        # Use this if you only have one json file named "style.json" inside the root directory, "json" directory or "jsonstyles" folder.
        # loadJsonStyle(self, self.ui) 

        # Use this to specify your json file(s) path/name
        loadJsonStyle(self, self.ui, jsonFiles = {
            "json-styles/main.json"
        })
        
        #######################################################################
        ## SHOW WINDOW
        #######################################################################
        self.show() 

        ########################################################################
        ## UPDATE APP SETTINGS LOADED FROM JSON STYLESHEET 
        ## IT'S IMPORTANT TO RUN THIS AFTER SHOWING THE WINDOW
        ## THIS PROCESS WILL RUN ON A SEPARATE THREAD WHEN GENERATING NEW ICONS
        ## TO PREVENT THE WINDOW FROM BEING UNRESPONSIVE
        ########################################################################
        # self = QMainWindow class
        QAppSettings.updateAppSettings(self)
        
        ########################################################################
        ## APPLICATION FUNCTIONS AND EVENTS
        ## APPLY SOME OTHER CONFIG TO WINDOW 
        ########################################################################
        self.app_functions = GUI_Functions(self)

        self.server = Server_Handler(self)
        # server.add_client_to_tree()


    ########################################################################
    ## GET THE THEME CHANGE PROGRESS
    ########################################################################
    def sassCompilationProgress(self, n):
        self.ui.themeProgress.setValue(n)


########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
########################################################################
## END
########################################################################  
