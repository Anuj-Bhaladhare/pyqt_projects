import PyQt5.QtWidgets as qt_widget
import PyQt5.QtGui as qt_gui
from back_end.auth import user_sign_up
from PyQt5 import uic
import sys
import os

class UI_OpenImage(qt_widget.QMainWindow):
    def __init__(self):
        super(UI_OpenImage, self).__init__()

        # Load the ui file
        ui_path = os.path.join(os.path.dirname(__file__), "./front_end/ui/singup.ui")
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"UI file not found at: {ui_path}")
        uic.loadUi(ui_path, self)

        # Define our widgets
        self.persion_name = self.findChild(qt_widget.QLineEdit, "lineEdit")
        self.persion_last_name = self.findChild(qt_widget.QLineEdit, "lineEdit_2")
        self.persion_email_name = self.findChild(qt_widget.QLineEdit, "lineEdit_3")
        self.persion_pass_name = self.findChild(qt_widget.QLineEdit, "lineEdit_4")

        self.sing_up_button = self.findChild(qt_widget.QPushButton, "pushButton")

        # Connect button to function
        self.sing_up_button.clicked.connect(self.user_sign_up)

        # Show the app window
        self.show()

    def user_sign_up(self):
        user_sign_up(self.persion_name.text(), self.persion_last_name.text(), self.persion_email_name.text(), self.persion_pass_name.text())



def main():
    # Initialize the App
    app = qt_widget.QApplication(sys.argv)
    window = UI_OpenImage()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

