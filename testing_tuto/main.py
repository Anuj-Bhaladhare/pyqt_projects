from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    def initUI(self):
        label = QtWidgets.QLabel(self)
        label.setText("Anuj First Lable")
        label.move(50, 50)

        b1 = QtWidgets.QPushButton(win)
        b1.setText("Click me")
        


def clicked():
    print("clicked")


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("this is the App")

    label = QtWidgets.QLabel(win)
    label.setText("My First Lable")
    label.move(50, 50)

    b1 = QtWidgets.QPushButton(win)
    b1.setText("Click Me")
    b1.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec_())

window()