from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QHBoxLayout
import sys
from PyQt5.QtGui import QIcon
from PyQt5 import uic

class window(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./h_box_layout.ui', self)

        # self.setGeometry(200, 200, 200, 200)
        # self.setWindowTitle("PyQt5 VBoxLayout")
        # self.setWindowIcon(QIcon('./asset/logo-icon-png-8.png'))

        # hbox = QHBoxLayout()

        # btn1 = QPushButton("Click One")
        # btn2 = QPushButton("Click Tow")
        # btn3 = QPushButton("Click Three")
        # btn4 = QPushButton("Click Four")

        # hbox.addWidget(btn1)
        # hbox.addWidget(btn2)
        # hbox.addWidget(btn3)
        # hbox.addWidget(btn4)

        # self.setLayout(hbox)


# if __name__ == '__main__':
app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec_())
    