from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def click_button():
    print("Clicked the BVutton")

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 800, 500)

    lable = QtWidgets.QLabel(win)
    lable.setText("this is the my first lable")
    lable.move(50, 50)

    btn1 = QtWidgets.QPushButton(win)
    btn1.setText("Click Me")
    btn1.clicked.connect(click_button)    # Button Connection

    win.show()
    sys.exit(app.exec_())

window()

