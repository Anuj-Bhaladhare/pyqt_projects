from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys
import os

class UI_OpenImage(QMainWindow):
    def __init__(self):
        super(UI_OpenImage, self).__init__()

        # Load the ui file
        ui_path = os.path.join(os.path.dirname(__file__), "./tic_tac_toe.ui")
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"UI file not found at: {ui_path}")
        uic.loadUi(ui_path, self)

        # Define A Counter To Keep Track of Who's Turn It IS 
        self.counter = 0

        # Define our widgets
        self.button_1 = self.findChild(QPushButton, "pushButton_001")
        self.button_2 = self.findChild(QPushButton, "pushButton_002")
        self.button_3 = self.findChild(QPushButton, "pushButton_003")
        self.button_4 = self.findChild(QPushButton, "pushButton_004")
        self.button_5 = self.findChild(QPushButton, "pushButton_005")
        self.button_6 = self.findChild(QPushButton, "pushButton_006")
        self.button_7 = self.findChild(QPushButton, "pushButton_007")
        self.button_8 = self.findChild(QPushButton, "pushButton_008")
        self.button_9 = self.findChild(QPushButton, "pushButton_009")
        self.start_button = self.findChild(QPushButton, "startPushButton")
        self.lable = self.findChild(QLabel, "label")

        # Clicked the Button
        self.button_1.clicked.connect(lambda: self.clicked_button(self.button_1))
        self.button_2.clicked.connect(lambda: self.clicked_button(self.button_2))
        self.button_3.clicked.connect(lambda: self.clicked_button(self.button_3))
        self.button_4.clicked.connect(lambda: self.clicked_button(self.button_4))
        self.button_5.clicked.connect(lambda: self.clicked_button(self.button_5))
        self.button_6.clicked.connect(lambda: self.clicked_button(self.button_6))
        self.button_7.clicked.connect(lambda: self.clicked_button(self.button_7))
        self.button_8.clicked.connect(lambda: self.clicked_button(self.button_8))
        self.button_9.clicked.connect(lambda: self.clicked_button(self.button_9))

        self.start_button.clicked.connect(self.resate_function)
        
        # Verify widgets were found

        # Connect the button to the click function

        # Show the app window
        self.show()


    # ================ Add The Function ===============
    def checkWin(self):
        if self.button_1.text() == self.button_2.text() and self.button_2.text() == self.button_3.text() and self.button_1.text() != ""  and self.button_2.text() != ""  and self.button_3.text() != "":
            self.win(self.button_1, self.button_2, self.button_3)
            self.desable_all_button()
        elif self.button_4.text() == self.button_5.text() and self.button_5.text() == self.button_6.text() and self.button_4.text() != ""  and self.button_5.text() != ""  and self.button_6.text() != "":
            self.win(self.button_6, self.button_4, self.button_5)
            self.desable_all_button()
        elif self.button_7.text() == self.button_8.text() and self.button_8.text() == self.button_9.text() and self.button_7.text() != ""  and self.button_8.text() != ""  and self.button_9.text() != "":
            self.win(self.button_7, self.button_8, self.button_9)
            self.desable_all_button()
        elif self.button_1.text() == self.button_4.text() and self.button_4.text() == self.button_7.text() and self.button_1.text() != ""  and self.button_4.text() != ""  and self.button_7.text() != "":
            self.win(self.button_1, self.button_4, self.button_7)
            self.desable_all_button()
        elif self.button_2.text() == self.button_5.text() and self.button_5.text() == self.button_8.text() and self.button_2.text() != ""  and self.button_5.text() != ""  and self.button_8.text() != "":
            self.win(self.button_5, self.button_2, self.button_8)
            self.desable_all_button()
        elif self.button_3.text() == self.button_6.text() and self.button_6.text() == self.button_9.text() and self.button_3.text() != ""  and self.button_6.text() != ""  and self.button_9.text() != "":
            self.win(self.button_9, self.button_6, self.button_3)
            self.desable_all_button()
        elif self.button_1.text() == self.button_5.text() and self.button_5.text() == self.button_9.text() and self.button_3.text() != ""  and self.button_5.text() != ""  and self.button_7.text() != "":
            self.win(self.button_1, self.button_5, self.button_9)
            self.desable_all_button()
        elif self.button_3.text() == self.button_5.text() and self.button_5.text() == self.button_7.text() and self.button_1.text() != ""  and self.button_5.text() != ""  and self.button_9.text() != "":
            self.win(self.button_3, self.button_5, self.button_7)
            self.desable_all_button()


    # Add Color to Win Line
    def win(self, a, b, c):
        # Add Winner
        self.lable.setText(f"Wow! '{a.text()}' is Win ")

        # Change Button color
        a.setStyleSheet("color: red;")
        b.setStyleSheet("color: red;")
        c.setStyleSheet("color: red;")

    # Desabled the all button
    def desable_all_button(self):
        button_list = [
            self.button_1,
            self.button_2,
            self.button_3,
            self.button_4,
            self.button_5,
            self.button_6,
            self.button_7,
            self.button_8,
            self.button_9
        ]
        for button in button_list:
            button.setEnabled(False)


    def clicked_button(self, b):
        if self.counter % 2 == 0:
            mark = "X"
            self.lable.setText(" 'O' Turn's ")
            self.counter+=1
        else:
            mark = "O"
            self.lable.setText(" 'X' Turn's ")
            self.counter+=1
        
        b.setText(mark)
        b.setEnabled(False)
        # Checked Win
        self.checkWin()

    def resate_function(self):
        button_list = [
            self.button_1,
            self.button_2,
            self.button_3,
            self.button_4,
            self.button_5,
            self.button_6,
            self.button_7,
            self.button_8,
            self.button_9
        ]
        for button in button_list:
            button.setText("")
            # set button color black
            button.setStyleSheet("color: black;")
            # button is Enabled
            button.setEnabled(True)

        # Resate the Counter
        self.counter = 0
        # Resate Indicator
        self.lable.setText(" X Goes First! ")



def main():
    # Initialize the App
    app = QApplication(sys.argv)
    window = UI_OpenImage()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()




# =====================  1st Type  ========================
    # self.button_1.clicked.connect(lambda: self.clicker(self.button_1))
    # self.button_2.clicked.connect(lambda: self.clicker(self.button_2))
    # self.button_3.clicked.connect(lambda: self.clicker(self.button_3))
    # self.button_4.clicked.connect(lambda: self.clicker(self.button_4))
    # self.button_5.clicked.connect(lambda: self.clicker(self.button_5))
    # self.button_6.clicked.connect(lambda: self.clicker(self.button_6))
    # self.button_7.clicked.connect(lambda: self.clicker(self.button_7))
    # self.button_8.clicked.connect(lambda: self.clicker(self.button_8))
    # self.button_9.clicked.connect(lambda: self.clicker(self.button_9))
    # self.button_10.clicked.connect(lambda: self.clicker(self.button_10))


# =====================  2nd Type  ========================
    # self.button_1.clicked.connect(self.clicked_button_1)
    # self.button_2.clicked.connect(self.clicked_button_2)
    # self.button_3.clicked.connect(self.clicked_button_3)
    # self.button_4.clicked.connect(self.clicked_button_4)
    # self.button_5.clicked.connect(self.clicked_button_5)
    # self.button_6.clicked.connect(self.clicked_button_6)
    # self.button_7.clicked.connect(self.clicked_button_7)
    # self.button_8.clicked.connect(self.clicked_button_8)
    # self.button_9.clicked.connect(self.clicked_button_9)
    # self.start_button.clicked.connect(self.start_button_10)

