import os
from PyQt5 import uic
from controllers.login_controller import LoginController
from PyQt5.QtWidgets import QMainWindow, QPushButton

class LoginScreenView(QMainWindow):
    def __init__(self):
        super(LoginScreenView, self).__init__()

        # Load the .ui file from the /ui directory
        ui_path = os.path.join(os.path.dirname(__file__), "..", "ui", "login_screen.ui")
        ui_path = os.path.abspath(ui_path)
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"UI file not found at: {ui_path}")
        uic.loadUi(ui_path, self)

        # ----------- PushButtons ------------
        self.navigate_singup_btn = self.findChild(QPushButton, "navigate_singup_btn")
        self.login_btn = self.findChild(QPushButton, "login_btn")

        # Setup Controller
        self.controller = LoginController(self)
        self.controller.setup_connection()