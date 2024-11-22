from PySide6.QtCore import QSettings, Qt
from PySide6.QtWidgets import QWidget
from src.ui_settings import Ui_Form

class SettingsWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.setWindowTitle("Settings")
        self.setWindowModality(Qt.NonModal)
        
        self.settings = QSettings()
        
