from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import QFileSystemWatcher
from PyQt6.QtGui import QFont, QTextBlockFormat, QTextCursor
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QTextCursor


class MainWindow(QMainWindow):
    def __init__(self,name = ""):
        super(MainWindow, self).__init__()

        # Set up the main window
        self.setObjectName(f"Keylog")
        self.resize(800, 600)
        self.filename = name

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
    def addLine(self,line):
        self.textEdit.append(line)
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        self.textEdit.setTextCursor(cursor)


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
    window.readfile()
    sys.exit(app.exec())
