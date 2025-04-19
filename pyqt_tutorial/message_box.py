from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(661, 463)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 601, 291))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # Create Button
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setText("Click Me")
        self.btn.move(50, 50)
        self.btn.clicked.connect(self.show_pop)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 661, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "This is the BOX"))

    def show_pop(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)  # ✅ Fix here
        msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Retry |  QMessageBox.Yes)
        msg.setWindowTitle("Tutorial of PyQt5")
        msg.setText("Your System Will Be Hacked!")
        msg.setDefaultButton(QMessageBox.Ignore)
        msg.setInformativeText("this is the informative text, ya!")
        msg.setDetailedText("this is the importatn details")

        msg.buttonClicked.connect(self.popup_button)

        result = msg.exec_()

        if result == QMessageBox.Retry:
            print("User chose: Retry")
        elif result == QMessageBox.Cancel:
            print("User chose: Cancel")

    def popup_button(self, i):  # Returning the message
        print(i.text())


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())

window()







'''
QMessageBox.Ok

QMessageBox.Open

QMessageBox.Save

QMessageBox.Cancel

QMessageBox.Closed

QMessageBox.Yes

QMessageBox.No

QMessageBox.Abort

QMessageBox.Retry

QMessageBox.Ignore
        '''
