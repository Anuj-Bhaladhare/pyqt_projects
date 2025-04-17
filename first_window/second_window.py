import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QMainWindow
from PyQt5.QtGui import QIcon

# class WindowExample(QDialog):     # -> ? X         Window Controller  
# class WindowExample(QMainWindow):       # -> -  ❐  X     Window Controller  
class WindowExample(QWidget):       # -> -  ❐  X     Window Controller  
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("Update Device")                      # Add the Title Name
        self.setWindowIcon(QIcon('./asset/logo-icon-png-8.png'))  # Add the LoGo

        self.create_button()
        self.show()

    def create_button(self):
        btn1 = QPushButton("Click Me", self)
        btn1.setText("Our Second Text")
        # btn1.move(200, 200)
        btn1.setGeometry(100, 300, 300, 100)
        btn1.setIcon(QIcon('./asset/button1.png'))
        btn1.setStyleSheet("background-color: red")
        btn1.clicked.connect(self.clicked_btn1)

        btn2 = QPushButton("Second Button", self)
        btn2.setGeometry(100, 400, 300, 100)
        btn2.setIcon(QIcon('./asset/button2.png'))
        btn2.setStyleSheet("background-color: blue")
        btn2.clicked.connect(self.clicked_btn2)
 
    def clicked_btn1(self):
        print("Button ONE Clicked")

    def clicked_btn2(self):
        print("Button TWO Clicked")

app = QApplication(sys.argv)
window = WindowExample()
sys.exit(app.exec_())
