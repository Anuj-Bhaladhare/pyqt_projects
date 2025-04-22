from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QMdiArea, QMdiSubWindow, QTextEdit
from PyQt5 import uic
import sys
import os

class UI_OpenImage(QMainWindow):
    count = 0  # ✅ Fixed: Add a class-level variable to track sub window count

    def __init__(self):
        super(UI_OpenImage, self).__init__()

        # ✅ Fixed: Proper UI path using os.path (relative to this script)
        ui_path = os.path.join(os.path.dirname(__file__), "multi_window.ui")
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"UI file not found at: {ui_path}")
        uic.loadUi(ui_path, self)

        # ✅ Correctly find widgets by objectName from the .ui file
        self.button_push = self.findChild(QPushButton, "pushButton")
        self.mdiArea = self.findChild(QMdiArea, "mdiArea")

        # ✅ Connect button to function
        self.button_push.clicked.connect(self.add_window)

        self.show()

    def add_window(self):
        # ✅ Fix: reference the class variable properly
        UI_OpenImage.count += 1

        # Create Sub Window
        sub = QMdiSubWindow()

        # Set a QTextEdit as the widget inside the subwindow
        sub.setWidget(QTextEdit())

        # ✅ Fix: Use setWindowTitle, not setWindowFilePath
        sub.setWindowTitle("Sub Window " + str(UI_OpenImage.count))

        # Add subwindow to MDI area
        self.mdiArea.addSubWindow(sub)
        sub.show()  # ✅ Fix: you need to call .show() on the subwindow

def main():
    app = QApplication(sys.argv)
    window = UI_OpenImage()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
