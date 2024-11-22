from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QFont
from PIL import Image
import io
BUFFER_SIZE = 1024 * 128
SEPARATOR = "<sep>"
class TerminalWindow(QtWidgets.QMainWindow):
    enterPressed = QtCore.pyqtSignal(str)
    def __init__(self,socket = None):
        super().__init__()
        self.setObjectName("TerminalWindow")
        self.resize(860, 781)
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 70, 841, 501))
        self.textEdit.setStyleSheet("background-color: #282828; color: #ffffff;")

        font = QFont()
        font.setFamily("Arial")  # Font family
        font.setPointSize(12)  # Font size
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        # self.textEdit.enterPressed.connect(self.processInput)
        self.cmd = ""


        self.socket = socket

        self.menubar = QtWidgets.QMenuBar(self)
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.textEdit.installEventFilter(self)
        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Terminal"))
        self.textEdit.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))




    def print_text(self, text):
        self.textEdit.setReadOnly(True)

        self.textEdit.append(text)  # Add text to the QTextEdit

        # After printing, switch back to editable
        self.textEdit.setReadOnly(False)

        # Move the cursor to the end to keep it editable
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.MoveOperation.End)
        self.textEdit.setTextCursor(cursor)

    def eventFilter(self, source, event):
        if source == self.textEdit and event.type() == QtCore.QEvent.Type.KeyPress:
            if event.key() == QtCore.Qt.Key.Key_Return or event.key() == QtCore.Qt.Key.Key_Enter:
                text = self.textEdit.toPlainText()
                last_line = text.splitlines()[-1]
                command = last_line.split("$>")[-1].strip()
                if(command == "clear"):
                    self.textEdit.setPlainText("")
                    self.print_text(f"{self.cmd} $>")
                elif command:
                    self.remote_shell(command)
                elif command == "":
                    self.print_text(f"{self.cmd} $>")
                return True
        return super().eventFilter(source, event)

    def remote_shell(self,command):
            self.socket.send(command.encode())
            output = self.socket.recv(BUFFER_SIZE).decode()
            print(f"{output} remote_shell")
            str1, str2 = output.split(SEPARATOR)

            if (str2 == 'image'):
                img_size = int(str1)
                img_data = b''
                while len(img_data) < img_size:
                    packet = self.socket.recv(4096)
                    if not packet:
                        break
                    img_data += packet
                img = Image.open(io.BytesIO(img_data))
                img.show()
                self.print_text(f"{self.cmd} $>")
            else:
                results, cwd = output.split(SEPARATOR)
                self.cmd = cwd
                self.print_text(results)
                self.print_text(cwd + " $>")
    def screen_shot(self,command):
        self.socket.send(command.encode())
        output = self.socket.recv(BUFFER_SIZE).decode()
        print(f"{output} remote_shell")
        str1, str2 = output.split(SEPARATOR)

        if (str2 == 'image'):
            img_size = int(str1)
            img_data = b''
            while len(img_data) < img_size:
                packet = self.socket.recv(4096)
                if not packet:
                    break
                img_data += packet
            img = Image.open(io.BytesIO(img_data))
            img.show()
            self.print_text(f"{self.cmd} $>")





if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    terminal_window = TerminalWindow()
    terminal_window.show()
    sys.exit(app.exec())
