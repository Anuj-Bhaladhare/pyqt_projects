from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
import sys
from PyQt5.QtGui import QIcon


class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("PyQt5 VBoxLayout")
        self.setWindowIcon(QIcon('python.png'))

        vbox = QVBoxLayout()

        btn1 = QPushButton("Clicked One", self)
        btn2 = QPushButton("Clicked Two", self)
        btn3 = QPushButton("Clicked Three", self)
        btn4 = QPushButton("Clicked Four", self)

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)

        self.setLayout(vbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = window()
    window.show()
    sys.exit(app.exec_())
    

