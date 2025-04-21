# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\qt_designer\ui\to_do_list_database.ui'
# Created by: PyQt5 UI code generator 5.15.11

import os
import sqlite3
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

# Ensure database folder exists
db_folder = os.path.join(os.path.dirname(__file__), '../database')
os.makedirs(db_folder, exist_ok=True)

# Create full path to the database
db_path = os.path.join(db_folder, 'mylist.db')

# Create the database and table if it doesn't exist
with sqlite3.connect(db_path) as conn:
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS todo_list (
            list_item TEXT
        )
    """)
    conn.commit()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(541, 507)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 10, 501, 81))
        self.lineEdit.setObjectName("lineEdit")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 160, 501, 301))
        self.listWidget.setObjectName("listWidget")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 110, 501, 30))
        self.widget.setObjectName("widget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.add_item_btn = QtWidgets.QPushButton(self.widget)
        self.add_item_btn.setObjectName("add_item_btn")
        self.add_item_btn.clicked.connect(self.add_it)
        self.horizontalLayout.addWidget(self.add_item_btn)

        self.delete_item_btn = QtWidgets.QPushButton(self.widget)
        self.delete_item_btn.setObjectName("delete_item_btn")
        self.delete_item_btn.clicked.connect(self.delete_it)
        self.horizontalLayout.addWidget(self.delete_item_btn)

        self.clear_the_list = QtWidgets.QPushButton(self.widget)
        self.clear_the_list.setObjectName("clear_the_list")
        self.clear_the_list.clicked.connect(self.clear_it)
        self.horizontalLayout.addWidget(self.clear_the_list)

        self.save_to_database = QtWidgets.QPushButton(self.widget)
        self.save_to_database.setObjectName("save_to_database")
        self.save_to_database.clicked.connect(self.save_data_base)
        self.horizontalLayout.addWidget(self.save_to_database)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 541, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Load items from database
        self.grab_all()

    def grab_all(self):
        with sqlite3.connect('./database/mylist.db') as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM todo_list")
            records = c.fetchall()
            for item in records:
                self.listWidget.addItem(item[0])

    def add_it(self):
        item = self.lineEdit.text()
        if item.strip() != "":
            self.listWidget.addItem(item)
            self.lineEdit.setText("")

    def delete_it(self):
        current_row = self.listWidget.currentRow()
        if current_row >= 0:
            self.listWidget.takeItem(current_row)

    def clear_it(self):
        self.listWidget.clear()

    def save_data_base(self):
        with sqlite3.connect('./database/mylist.db') as conn:
            c = conn.cursor()
            c.execute('DELETE FROM todo_list')

            items = [self.listWidget.item(i).text() for i in range(self.listWidget.count())]
            for item in items:
                c.execute("INSERT INTO todo_list (list_item) VALUES (?)", (item,))
            conn.commit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "To-Do List"))
        self.add_item_btn.setText(_translate("MainWindow", "Add Item To List"))
        self.delete_item_btn.setText(_translate("MainWindow", "Delete Item From List"))
        self.clear_the_list.setText(_translate("MainWindow", "Clear The List"))
        self.save_to_database.setText(_translate("MainWindow", "Save to Database"))

def window():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

window()
