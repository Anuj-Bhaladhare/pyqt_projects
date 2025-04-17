from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import uic
import sys

class UI(QWidget):       # Header File
    def __init__(self):
        super().__init__()
        uic.loadUi("buttonTest.ui", self)

        # find our widgets
        button = self.findChild(QPushButton, 'pushButton')
        button.clicked.connect(self.clicked_btn)

    def clicked_btn():
        print("this is the button clicked")



app = QApplication([])
window = UI()

window.show()

