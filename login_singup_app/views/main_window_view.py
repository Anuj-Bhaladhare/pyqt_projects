import os
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QPushButton, QStackedWidget
from controllers.main_controller import MainController

class MainWindowView(QMainWindow):
    def __init__(self):
        super(MainWindowView, self).__init__()

        # Load the .ui file from the /ui directory
        ui_path = os.path.join(os.path.dirname(__file__), "..", "ui", "main_window.ui")
        ui_path = os.path.abspath(ui_path)
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"UI file not found at: {ui_path}")
        uic.loadUi(ui_path, self)

        # ----------- PushButtons ------------
        self.home_push_button = self.findChild(QPushButton, "home_button")
        self.login_push_button = self.findChild(QPushButton, "login_button")
        self.singup_push_button = self.findChild(QPushButton, "sing_up_button")
        self.user_push_button = self.findChild(QPushButton, "user_button")

        # Container for Swithing Page
        self.main_body_container = self.findChild(QStackedWidget, "mainStack")

        # Debug: Check if buttons were loaded
        print("[DEBUG] home_push_button:", self.home_push_button)
        print("[DEBUG] login_push_button:", self.login_push_button)

        # Setup Controller
        self.controller = MainController(self)
        self.controller.setup_connection()


