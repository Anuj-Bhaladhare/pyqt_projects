from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys
import os

class UI_OpenImage(QMainWindow):
    def __init__(self):
        super(UI_OpenImage, self).__init__()

        # Load the ui file
        ui_path = os.path.join(os.path.dirname(__file__), "./open_image.ui")
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"UI file not found at: {ui_path}")
        uic.loadUi(ui_path, self)

        # Define our widgets
        self.button = self.findChild(QPushButton, "pushButton")
        self.label = self.findChild(QLabel, "label")
        
        # Verify widgets were found
        if not self.button or not self.label:
            raise ValueError("Required widgets (pushButton or label) not found in UI file")

        # Connect the button to the click function
        self.button.clicked.connect(self.click_button)

        # Show the app window
        self.show()

    def click_button(self):
        # Open file dialog to select an image
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Open Image File",
            "",  # Start in the user's home directory
            "Image Files (*.png *.jpg *.jpeg *.bmp *.gif);;All Files (*)"
        )

        if file_name:
            pixmap = QPixmap(file_name)
            if pixmap.isNull():
                print(f"Failed to load image: {file_name}")
                return
            self.label.setPixmap(pixmap)
            self.label.setScaledContents(True)  # Scale image to fit label

def main():
    # Initialize the App
    app = QApplication(sys.argv)
    window = UI_OpenImage()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

