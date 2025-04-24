import os
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QPushButton
from controllers.singup_controller import SingUpController

class SingupScreenView(QMainWindow):
    def __init__(self):
        super(SingupScreenView, self).__init__()

        # Load the .ui file from the /ui directory
        ui_path = os.path.join(os.path.dirname(__file__), "..", "ui", "sing_up_screen.ui")
        ui_path = os.path.abspath(ui_path)
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"UI file not found at: {ui_path}")
        uic.loadUi(ui_path, self)

        # ----------- PushButtons ------------
        self.navigate_login_btn = self.findChild(QPushButton, "navigate_login_btn")
        self.sing_up_btn = self.findChild(QPushButton, "sing_up_btn")

        # Setup Controller
        self.controller = SingUpController(self)
        self.controller.setup_connection()