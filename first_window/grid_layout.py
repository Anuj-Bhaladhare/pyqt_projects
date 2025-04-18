from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sys

class UI(QMainWindow):  # 🔥 This must match the .ui file's top-level widget
    def __init__(self):
        super().__init__()
        uic.loadUi('./grid_layout_gui.ui', self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec_())


    









# from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
# from PyQt5.QtGui import QIcon
# from PyQt5 import uic
# import sys


# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi('./grid_layout_gui.ui', self)

#         # self.setGeometry(200, 200, 400, 300)
#         # self.setWindowTitle("PyQt5 GridLayout")
#         # self.setWindowIcon(QIcon("./asset/logo-icon-png-8.png"))

#         # grid = QGridLayout()

#         # btn1 = QPushButton("Click One")
#         # btn2 = QPushButton("Click Two")
#         # btn3 = QPushButton("Click Three")
#         # btn4 = QPushButton("Click Four")
#         # btn5 = QPushButton("Click Five")
#         # btn6 = QPushButton("Click Six")
#         # btn7 = QPushButton("Click Seven")
#         # btn8 = QPushButton("Click Eight")

#         # grid.addWidget(btn1, 0, 0)
#         # grid.addWidget(btn2, 0, 1)
#         # grid.addWidget(btn3, 0, 2)
#         # grid.addWidget(btn4, 0, 3)
#         # grid.addWidget(btn5, 1, 0)
#         # grid.addWidget(btn6, 1, 1)
#         # grid.addWidget(btn7, 1, 2)
#         # grid.addWidget(btn8, 1, 3)

#         # self.setLayout(grid)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


