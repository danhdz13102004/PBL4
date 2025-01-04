from PySide6.QtCore import Qt, QSize, QPoint, QRect, QObject
from PySide6.QtWidgets import QWidget, QMainWindow, QSizeGrip, QGraphicsDropShadowEffect, QApplication
from PySide6.QtGui import QIcon, QFont, QCursor, QColor

class Window_Utils:
    def __init__(self, window, config=None):
        self.main: QMainWindow = window
        ## Mouse position
        self._mouse_pos = None
        self._window_state = {
            "is_maximized": False,
            "restore_geometry": None,
            "mouse_pressed": False
        }

        ## Add window flag to allow resize
        self.main.setWindowFlags(Qt.WindowType.Window)

        self.default_config = {
            "title": "Server",
            "icon": "D:/PBL4/Keylogger/server/Qss/icons/Icons/font_awesome/brands/python.png",
            "frameless": True,
            "translucentBg": True,
            "sizeGrip": "sizeGrip",
            "shadow": [{
                "color": "#fff",
                "blurRadius": 20,
                "xOffset": 0,
                "yOffset": 0,
                "centralWidget": "styleSheet"
            }],
            "navigation": [{
                "minimize": "minimizeAppBtn",
                "close": "closeAppBtn",
                "restore": [{
                    "buttonName": "restoreAppBtn",
                    "normalIcon": "D:/PBL4/Keylogger/server/Qss/icons/black/material_design/zoom_out_map.png",
                    "maximizedIcon": "D:/PBL4/Keylogger/server/Qss/icons/black/material_design/zoom_in_map.png"
                }],
                "moveWindow": "titleBarWidget",
                "titleBar": "titleBarWidget"
            }]
        }
        self.config = self.default_config.copy()
        if config:
            self.deep_update(self.config, config)
        self.config_window()

    def deep_update(self, d, u):
        for k, v in u.items():
            if isinstance(v, dict) and k in d:
                self.deep_update(d[k], v)
            else:
                d[k] = v

    def config_window(self):
        if self.config.get("title"):
            self.set_window_title(self.config["title"])

        if self.config.get("icon"):
            self.set_window_icon(self.config["icon"])

        if self.config.get("frameless"):
            self.set_frameless_window()

        if self.config.get("translucentBg"):
            self.set_translucent_background()

        # Setup window flags for resizable frameless window
        self.main.setWindowFlags(
            self.main.windowFlags() |
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowMinMaxButtonsHint
        )

        if self.config.get("sizeGrip"):
            self.add_size_grip()

        if self.config.get("shadow"):
            self.add_shadow_effect()

        if self.config.get("navigation"):
            self.configure_navigation()

    def set_window_title(self, title):
        self.main.setWindowTitle(str(title))
        return self.main

    def set_window_icon(self, icon_path):
        try:
            icon = QIcon(icon_path)
            if not icon.isNull():
                self.main.setWindowIcon(icon)
            else:
                print(f"Error: Icon '{icon_path}' not found or invalid.")
        except Exception as e:
            print(f"Error setting window icon: {str(e)}")
        return self.main

    def set_frameless_window(self):
        self.main.setWindowFlags(
            self.main.windowFlags() |
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowMinMaxButtonsHint
        )
        return self.main

    def set_translucent_background(self):
        self.main.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        return self.main

    def add_size_grip(self):
        try:
            size_grip_name = self.config["sizeGrip"]
            size_grip = self.main.findChild(QWidget, size_grip_name)
            if size_grip:
                grip = QSizeGrip(size_grip)
                grip.setStyleSheet("background: transparent")
                size_grip.raise_()  ## Always on the top
            else:
                print(f"Warning: Size grip widget '{size_grip_name}' not found.")
        except Exception as e:
            print(f"Error adding size grip: {str(e)}")
        return self.main

    def add_shadow_effect(self):
        try:
            for shadow in self.config["shadow"]:
                color = shadow.get("color", "#000")
                blur_radius = shadow.get("blurRadius", 20)
                x_offset = shadow.get("xOffset", 0)
                y_offset = shadow.get("yOffset", 0)
                central_widget_name = shadow.get("centralWidget", "")
                central_widget = self.main.findChild(QWidget, central_widget_name)
                if central_widget:
                    effect = QGraphicsDropShadowEffect()
                    effect.setColor(QColor(color))
                    effect.setBlurRadius(blur_radius)
                    effect.setXOffset(x_offset)
                    effect.setYOffset(y_offset)
                    central_widget.setGraphicsEffect(effect)
                else:
                    print(f"Warning: Central widget '{central_widget_name}' not found for shadow.")
        except Exception as e:
            print(f"Error adding shadow effect: {str(e)}")

    def configure_navigation(self):
        try:
            for nav in self.config["navigation"]:
                if minimize_btn := nav.get("minimize"):
                    self.bind_button(minimize_btn, self.minimize_window)

                if close_btn := nav.get("close"):
                    self.bind_button(close_btn, self.close_window)

                for restore in nav.get("restore", []):
                    button_name = restore.get("buttonName")
                    normal_icon = restore.get("normalIcon")
                    maximized_icon = restore.get("maximizedIcon")
                    if button_name:
                        self.bind_restore_button(button_name, normal_icon, maximized_icon)

                if move_widget := nav.get("moveWindow"):
                    self.enable_window_movement(move_widget)
        except Exception as e:
            print(f"Error configuring navigation: {str(e)}")

    def bind_button(self, button_name, callback):
        if button := self.main.findChild(QWidget, button_name):
            button.clicked.connect(callback)
        else:
            print(f"Warning: Button '{button_name}' not found.")

    def enable_window_movement(self, title_bar_name):
        title_bar = self.main.findChild(QWidget, title_bar_name)
        if title_bar:
            title_bar.mousePressEvent = self._mouse_press_event
            title_bar.mouseDoubleClickEvent = self._mouse_double_click_event
            title_bar.mouseMoveEvent = self._mouse_move_event
            title_bar.mouseReleaseEvent = self._mouse_release_event
        else:
            print(f"Warning: Title bar widget '{title_bar_name}' not found.")

    ## Save position of mouse event when press on title bar
    def _mouse_press_event(self, event):
        if event.button() == Qt.LeftButton:
            self._window_state["mouse_pressed"] = True
            self._mouse_pos = event.globalPos() - self.main.pos()   ## Position of mouse and old position of window
            event.accept()

    ## Double click on title bar to minimize/maximize
    def _mouse_double_click_event(self, event):
        if event.button() == Qt.LeftButton:
            if self._window_state["is_maximized"]:
                self.restore_window()
            else:
                self.maximize_window()
            event.accept()

    ## Drag window in new position
    def _mouse_move_event(self, event):
        if event.buttons() == Qt.LeftButton and self._window_state["mouse_pressed"]:
            if self._window_state["is_maximized"]:
                ## Calculate ratio when drag window in maximized status
                ratio = event.globalPos().x() / self.main.width()
                self.restore_window()
                new_pos = QPoint(int(event.globalPos().x() - self.main.width() * ratio),
                                 event.globalPos().y() - self._mouse_pos.y())
                self.main.move(new_pos)
            else:
                self.main.move(event.globalPos() - self._mouse_pos)
            event.accept()

    def _mouse_release_event(self, event):
        self._window_state["mouse_pressed"] = False
        ## Maximize window when drag to the top of screen
        if event.globalPos().y() <= 5 and not self._window_state["is_maximized"]:
            self.maximize_window()
        event.accept()

    def minimize_window(self):
        self.main.showMinimized()

    def close_window(self):
        self.main.close()

    def bind_restore_button(self, button_name, normal_icon, maximized_icon):
        button = self.main.findChild(QWidget, button_name)
        if button:
            # Set initial icon
            if normal_icon:
                button.setIcon(QIcon(normal_icon))

            def toggle_window_state():
                if self._window_state["is_maximized"]:
                    self.restore_window()
                else:
                    self.maximize_window()

            # Disconnect old event
            try:
                button.clicked.disconnect()
            except (RuntimeError, TypeError):
                pass

            button.clicked.connect(toggle_window_state)
        else:
            print(f"Warning: Restore button '{button_name}' not found.")

    def maximize_window(self):
        if not self._window_state["is_maximized"]:
            self._window_state["restore_geometry"] = self.main.geometry()   ## Save old geometry to windowstate to restore
            screen = QApplication.primaryScreen().geometry()
            self.main.setGeometry(screen)
            self._window_state["is_maximized"] = True
            self.update_restore_button_icon(True)

    def restore_window(self):
        if self._window_state["is_maximized"] and self._window_state["restore_geometry"]:
            self.main.setGeometry(self._window_state["restore_geometry"])
            self._window_state["is_maximized"] = False
            self.update_restore_button_icon(False)

    def update_restore_button_icon(self, is_maximized):
        try:
            for nav in self.config["navigation"]:
                for restore in nav.get("restore", []):
                    button_name = restore.get("buttonName")
                    button = self.main.findChild(QWidget, button_name)
                    if button:
                        icon_path = restore.get("maximizedIcon" if is_maximized else "normalIcon")
                        if icon_path:
                            icon = QIcon(icon_path)
                            if not icon.isNull():
                                button.setIcon(icon)
                            else:
                                print(f"Warning: Failed to load icon from {icon_path}")
        except Exception as e:
            print(f"Error updating restore button icon: {str(e)}")