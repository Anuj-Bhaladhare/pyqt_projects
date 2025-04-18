# -*- coding: utf-8 -*-
# Generated from header_file.ui by pyuic5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(587, 427)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setText("Welcome to My App")
        self.label.setGeometry(QtCore.QRect(50, 150, 500, 100))
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 587, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")

        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")

        self.actionWindow1 = QtWidgets.QAction(MainWindow)
        self.actionWindow1.setObjectName("actionWindow1")

        self.actionWindow2 = QtWidgets.QAction(MainWindow)
        self.actionWindow2.setObjectName("actionWindow2")

        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuWindow.addAction(self.actionWindow1)
        self.menuWindow.addAction(self.actionWindow2)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())

        self.actionNew.triggered.connect(lambda: self.clicked("11111111111111111"))
        self.actionSave.triggered.connect(lambda: self.clicked("22222222222222222"))
        self.actionWindow1.triggered.connect(lambda: self.clicked("33333333333333333"))
        self.actionWindow2.triggered.connect(lambda: self.clicked("44444444444444444"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))

        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Open New File"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+S"))

        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save File"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+A"))

        self.actionWindow1.setText(_translate("MainWindow", "Window 1"))
        self.actionWindow1.setShortcut(_translate("MainWindow", "Ctrl+V"))

        self.actionWindow2.setText(_translate("MainWindow", "Window 2"))
        self.actionWindow2.setShortcut(_translate("MainWindow", "Ctrl+B"))

    def clicked(self, text):
    # def clicked(self):
        self.label.setText(text)
        self.label.adjustSize()
        print("Clicked...")

def window():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

window()
