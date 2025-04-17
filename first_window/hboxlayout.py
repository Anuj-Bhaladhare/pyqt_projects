from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
import sys
from PyQt5.QtGui import QIcon

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 200, 200)
        self.setWindowTitle("PyQt5 VBoxLayout")
        self.setWindowIcon(QIcon('./asset/logo-icon-png-8.png'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = window()
    window.show()
    sys.exit(app.exec_())
    