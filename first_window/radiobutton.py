from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QGroupBox, QHBoxLayout, QRadioButton, QVBoxLayout, QGridLayout, QLabel, QPushButton
import sys
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("PyQt5 QRadioButton")
        self.setWindowIcon(QIcon('./asset/button1.png'))

        self.create_radiobutton()  # call the function to create the UI

        # Add the GroupBox to the window layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupbox)

        # Label to show selected option
        self.label = QLabel("You Have Selected: ")
        self.label.setFont(QFont("Sanserif", 12))
        vbox.addWidget(self.label)

        self.setLayout(vbox)
    
    def create_radiobutton(self):
        self.groupbox = QGroupBox("What is the favorite sport ?")
        self.groupbox.setFont(QFont("Sanserif", 15))

        hbox = QHBoxLayout()

        self.rad1 = QRadioButton("Football")
        self.rad1.setChecked(True)
        self.rad1.setIcon(QIcon("./asset/button2.png"))
        self.rad1.setIconSize(QSize(40, 40))
        self.rad1.setFont(QFont("Sanserif", 14))
        self.rad1.toggled.connect(self.on_selected)
        hbox.addWidget(self.rad1)

        self.rad2 = QRadioButton("Cricket")
        # self.rad2.setChecked(True)
        self.rad2.setIcon(QIcon("./asset/button2.png"))
        self.rad2.setIconSize(QSize(40, 40))
        self.rad2.setFont(QFont("Sanserif", 14))
        self.rad2.toggled.connect(self.on_selected)
        hbox.addWidget(self.rad2)

        self.rad3 = QRadioButton("Tennis")
        # self.rad3.setChecked(True)
        self.rad3.setIcon(QIcon("./asset/button2.png"))
        self.rad3.setIconSize(QSize(40, 40))
        self.rad3.setFont(QFont("Sanserif", 14))
        self.rad3.toggled.connect(self.on_selected)
        hbox.addWidget(self.rad3)

        self.groupbox.setLayout(hbox)

    def on_selected(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            self.label.setText("You Have Selected: " + radio_button.text())
            print("Clicked: ", radio_button.text())


app = QApplication([])
window = Window()
window.show()
app.exec_()
