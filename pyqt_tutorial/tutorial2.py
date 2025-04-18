from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 800, 500)
        self.setWindowTitle("Tutorial 2 ANUJ")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("this is the Tutorial 2 Lable")
        self.label.move(50, 50)

        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText("Click Me!")
        self.btn.clicked.connect(self.clicked_button)

    def clicked_button(self):
        self.label.setText("this os tje UPDATED text mamu")
        self.update()
        print("Button is Clicked")

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
