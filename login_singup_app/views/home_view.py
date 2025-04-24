import os
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QPushButton

class HomeScreenView(QMainWindow):
    def __init__(self):
        super(HomeScreenView, self).__init__()

        # Load the .ui file from the /ui directory
        ui_path = os.path.join(os.path.dirname(__file__), "..", "ui", "home_screen.ui")
        ui_path = os.path.abspath(ui_path)
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"UI file not found at: {ui_path}")
        uic.loadUi(ui_path, self)