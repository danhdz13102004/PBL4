import sys
import socket
import json
from PyQt6.QtWidgets import QApplication, QMainWindow, QTreeView, QVBoxLayout, QWidget, QMenu
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QIcon, QAction
from PyQt6.QtCore import pyqtSignal, Qt, QPoint
SEPARATOR = "<sep>"

class FileManagerServer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Remote File Manager")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.tree_view = QTreeView()
        self.layout.addWidget(self.tree_view)

        self.model = QStandardItemModel()
        self.tree_view.setModel(self.model)

        # Load icons
        self.folder_icon = QIcon.fromTheme("folder")
        self.file_icon = QIcon.fromTheme("text-x-generic")

        self.tree_view.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tree_view.customContextMenuRequested.connect(self.show_context_menu)

        self.socket = None



    def setup_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('localhost', 12345))
        self.server_socket.listen(1)

        print("Server listening on localhost:12345")
        self.accept_connection()

    def accept_connection(self):
        client_socket, addr = self.server_socket.accept()
        print(f"Connection from {addr}")

        data = b""
        while True:
            chunk = client_socket.recv(4096)
            if not chunk:
                break
            data += chunk

        try:
            directory_tree = json.loads(data.decode())
            self.populate_tree_view(directory_tree)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            print(f"Received data: {data.decode()[:100]}...")  # Print first 100 characters of received data

        client_socket.close()

    def populate_tree_view(self, directory_tree, parent=None):
        if parent is None:
            parent = self.model.invisibleRootItem()

        for name, content in directory_tree.items():
            if isinstance(content, dict):
                item = QStandardItem(self.folder_icon, name)
                parent.appendRow(item)
                self.populate_tree_view(content, item)
            else:
                item = QStandardItem(self.file_icon, name)
                parent.appendRow(item)


    def show_context_menu(self, position: QPoint):
        # Get the item under the cursor
        index = self.tree_view.indexAt(position)
        if not index.isValid():
            return

        # Get the corresponding item from the model
        item = self.model.itemFromIndex(index)

        # Create the context menu
        menu = QMenu(self)

        # Add actions (e.g., open, delete, rename)
        download_action = QAction("Download", self)
        encrypt_action = QAction("Encrypt", self)
        decrypt_action = QAction("Decrypt", self)

        # Connect actions to methods
        download_action.triggered.connect(lambda: self.download(item))
        encrypt_action.triggered.connect(lambda: self.encrypt(item))
        decrypt_action.triggered.connect(lambda: self.decrypt(item))

        # Add actions to the menu
        menu.addAction(download_action)
        menu.addAction(encrypt_action)
        menu.addAction(decrypt_action)

        # Show the menu at the position where the right-click happened
        menu.exec(self.tree_view.viewport().mapToGlobal(position))

    def handling_item(self,item):
        print(item.text())

    def get_full_path(self, item):
        path = []
        while item is not None:
            path.insert(0, item.text())  # Insert the item name at the beginning
            item = item.parent()  # Move to the parent
        return "/".join(path)  # Join to create the full path

    def download(self,item):
        full_path = self.get_full_path(item)
        self.socket.send(f"download{SEPARATOR}{full_path}".encode())
        print(full_path)

    def encrypt(self,item):
        full_path = self.get_full_path(item)
        self.socket.send(f"en{SEPARATOR}{full_path}".encode())
        print(f"en {item.text()}")

    def decrypt(self,item):
        full_path = self.get_full_path(item)
        self.socket.send(f"de{SEPARATOR}{full_path}".encode())
        print(f"de {item.text()}")

