from lib2to3.fixes.fix_input import context

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import QFileSystemWatcher
from PyQt6.QtGui import QFont, QTextBlockFormat, QTextCursor
from PyQt6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self,name = ""):
        super(MainWindow, self).__init__()

        # Set up the main window
        self.setObjectName(f"Keylog")
        self.resize(800, 600)
        self.filename = name
        self.watcher = QFileSystemWatcher(self)
        self.watcher.addPath(self.filename)
        self.watcher.fileChanged.connect(self.on_file_changed)

        # Create central widget
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)



        # Create QTextEdit
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 10, 791, 571))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        # self.textEdit.
        font = QFont()
        font.setFamily("Arial")  # Font family
        font.setPointSize(12)  # Font size
        self.textEdit.setFont(font)
        self.set_line_spacing(1.5)
        # Create menubar
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

        # Create statusbar
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        # Set window title
        self.setWindowTitle("MainWindow")
    def readfile(self):
        try:
            if self.filename:
                with open(self.filename,'r',encoding='utf-8') as file:
                    content = file.read()
                self.textEdit.append(content)
        except Exception:
                self.textEdit.setText("")

    def on_file_changed(self, path):
        """Append new content when the file is changed."""
        try:
            with open(self.filename, 'r',encoding='utf-8') as file:
                content = file.read()

            # Clear the QTextEdit and set the new content
            self.textEdit.setText(content)
        except FileNotFoundError:
            # Handle case where the file is deleted or missing
            self.textEdit.append("File not found or deleted")

    def set_line_spacing(self, line_spacing_factor):
        """Set custom line spacing in QTextEdit."""
        cursor = self.textEdit.textCursor()
        block_format = QTextBlockFormat()

        # Set line height (1.0 is normal, values above 1 increase spacing)
        block_format.setLineHeight(line_spacing_factor * 100, 1)

        # Apply block format to all content
        cursor.select(QTextCursor.SelectionType.Document)
        cursor.setBlockFormat(block_format)
        cursor.clearSelection()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow("LAPTOP-4USQKFOM.txt")
    window.show()
    sys.exit(app.exec())
