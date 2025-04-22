from PyQt5.QtWidgets import QMainWindow, QApplication, QCalendarWidget, QPushButton, QLabel, QFileDialog
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys
import os

class UI_OpenImage(QMainWindow):
    def __init__(self):
        super(UI_OpenImage, self).__init__()

        # Load the ui file
        ui_path = os.path.join(os.path.dirname(__file__), "./calendar.ui")
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"UI file not found at: {ui_path}")
        uic.loadUi(ui_path, self)

        # Define our widgets
        self.calendar = self.findChild(QCalendarWidget, "calendarWidget")
        self.label = self.findChild(QLabel, "label")

        # connect the calander to the calander
        self.calendar.selectionChanged.connect(self.grab_date)

        # Show the app window
        self.show()

    # get date from calender
    def grab_date(self):
        dateSelected = self.calendar.selectedDate()

        # Put Date On Label
        self.label.setText(str(dateSelected.toPyDate()))

def main():
    # Initialize the App
    app = QApplication(sys.argv)
    window = UI_OpenImage()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
