from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys
import os

class UI_OpenImage(QMainWindow):
    def __init__(self):
        super(UI_OpenImage, self).__init__()

        # Load the ui file
        ui_path = os.path.join(os.path.dirname(__file__), "./interface.ui")
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"UI file not found at: {ui_path}")
        uic.loadUi(ui_path, self)

        # Define our widgets

        # Show the app window
        self.show()

def main():
    # Initialize the App
    app = QApplication(sys.argv)
    window = UI_OpenImage()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

