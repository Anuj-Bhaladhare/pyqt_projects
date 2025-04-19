# Creating the Vertual Envoirment in Python for the PyQt

1.  pip install virtualenv 
2.  python -m venv myenv
3.  myenv\Scripts\activate  -> [for Activat env]
4.  deactivate              -> [for DeActivat env]



C:\Users\anujb\AppData\Local\Programs\Python\Python312\Scripts
pyuic5 buttonTest.ui -o buttonexample.py 
{pyuic5 ../../buttonTest.ui -o buttonexample.py}    --> Command is Working


this also the working command :-> myenv\Scripts\pyuic5 source_file.ui -o result_file.py












# ================>> Template GUI <<================

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
        print("Button is Clicked")


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()










