from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QSettings, QPropertyAnimation, QEasingCurve, QParallelAnimationGroup

from .app_settings import App_Settings

from .ui_dashboard import Ui_MainWindow

class Sidebar_Utils:
    def __init__(self, main_window):
        self.main = main_window
        self.ui: Ui_MainWindow = main_window.ui
        self.settings = QSettings()

        ## Get settings from App_Settings.py
        self.sb_expanded_width = App_Settings.SB_EXPANDED_WIDTH
        self.sb_collapsed_width = App_Settings.SB_COLLAPSED_WIDTH
        self.animation_duration = App_Settings.SB_DURATION_ANIMATION

        self.animation_group = QParallelAnimationGroup()
    def load_sidebar_state(self):
        ## Load saved width, if not use SB_COLLAPSED WIDTH
        saved_width = self.settings.value("sidebar/width", App_Settings.SB_COLLAPSED_WIDTH, type=int)

        self.update_sidebar_width(saved_width)
        
        if saved_width <= self.sb_collapsed_width:
            for button in self.ui.sidebarWidget.findChildren(QPushButton):
                if not button.property("originalText"):
                    button.setProperty("originalText", button.text())
                button.setText("")

    def update_sidebar_width(self, width):
        ## Button's width has 10 units less than the widget's width
        ## Update widgets and buttons new width 
        for widget in [self.ui.sidebarWidget, self.ui.topSBWidget, self.ui.mainSBWidget]:
            widget.setFixedWidth(width)
            for button in widget.findChildren(QPushButton):
                button.setFixedWidth(width - 10)    

    def save_sidebar_state(self, width):
        self.settings.setValue("sidebar/width", width)
        App_Settings.SB_CURRENT_WIDTH = width

    def toggle_sidebar(self):
        current_width = self.ui.sidebarWidget.width()
        new_width = self.sb_expanded_width if current_width == self.sb_collapsed_width else self.sb_collapsed_width

        ## Save orginal text
        for button in self.ui.sidebarWidget.findChildren(QPushButton):
            if not button.property("originalText"):
                button.setProperty("originalText", button.text())
        
        ## Clear previous animations
        self.animation_group.clear()

        ## Animate widgets and buttons - Add animation to group
        self._animate_widget(self.ui.sidebarWidget, current_width, new_width)
        self._animate_widget(self.ui.mainSBWidget, current_width, new_width)
        self._animate_buttons(self.ui.sidebarWidget, current_width, new_width - 10)

        ## Save the new state after animation finishes
        self.animation_group.finished.connect(lambda: self.save_sidebar_state(new_width))

        # Start the animation group
        self.animation_group.start()

    def _animate_widget(self, widget, start_width, end_width):
        ## Create animations for widget
        anim_min = QPropertyAnimation(widget, b"minimumWidth")
        anim_min.setDuration(self.animation_duration)
        anim_min.setStartValue(start_width)
        anim_min.setEndValue(end_width)
        anim_min.setEasingCurve(QEasingCurve.InOutQuart)

        anim_max = QPropertyAnimation(widget, b"maximumWidth")
        anim_max.setDuration(self.animation_duration)
        anim_max.setStartValue(start_width)
        anim_max.setEndValue(end_width)
        anim_max.setEasingCurve(QEasingCurve.InOutQuart)

        self.animation_group.addAnimation(anim_min)
        self.animation_group.addAnimation(anim_max)

    def _animate_buttons(self, widget, start_width, end_width):
        ## Animate all buttons inside the widget
        for button in widget.findChildren(QPushButton):
            anim_button = QPropertyAnimation(button, b"minimumWidth")
            anim_button.setDuration(self.animation_duration)
            anim_button.setStartValue(start_width)
            anim_button.setEndValue(end_width)
            anim_button.setEasingCurve(QEasingCurve.InOutQuart)

            ## Hide textObject when collapsed and show when expanded
            if end_width <= self.sb_collapsed_width:
                button.setText("")
            else:
                button.setText(button.property("originalText"))
                
            self.animation_group.addAnimation(anim_button)
            