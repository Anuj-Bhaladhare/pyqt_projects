from PyQt5 import QtWidgetsh
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("this is the App")

    win.show()
    sys.exit(app.exec_())


window()

