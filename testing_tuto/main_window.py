from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(463, 299)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_click = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_click.setGeometry(QtCore.QRect(160, 160, 111, 31))
        self.pushButton_click.setStyleSheet(
            "background-color: blue;\n"
            "font-size: 20px;\n"
            "color: white;\n"
            "font-weight: bold;\n"
        )
        self.pushButton_click.setObjectName("pushButton_click")

        self.click_count_lable = QtWidgets.QLabel(self.centralwidget)
        self.click_count_lable.setGeometry(QtCore.QRect(130, 80, 171, 51))
        self.click_count_lable.setStyleSheet(
            "font-size: 15px;\n"
            "font-weight: bold;"
        )
        self.click_count_lable.setObjectName("click_count_lable")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_click.setText(_translate("MainWindow", "Click Me"))
        self.click_count_lable.setText(_translate("MainWindow", "Number of Click: "))
