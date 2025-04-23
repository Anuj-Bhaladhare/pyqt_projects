import PyQt5.QtWidgets as qt_widget
import PyQt5.QtGui as qt_gui
from PyQt5 import uic
import sys
import os
# from googletrans import Translator
import googletrans
import textblob

class UI_OpenImage(qt_widget.QMainWindow):
    def __init__(self):
        super(UI_OpenImage, self).__init__()

        # Load the ui file
        ui_path = os.path.join(os.path.dirname(__file__), "./translate.ui")
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"UI file not found at: {ui_path}")
        uic.loadUi(ui_path, self)

        # Define our widgets        
        self.text_box_1 = self.findChild(qt_widget.QTextEdit, "textEdit")
        self.text_box_2 = self.findChild(qt_widget.QTextEdit, "textEdit_3")

        self.combo_box_1 = self.findChild(qt_widget.QComboBox, "comboBox")
        self.combo_box_2 = self.findChild(qt_widget.QComboBox, "comboBox_2")

        self.trans_button = self.findChild(qt_widget.QPushButton, "pushButton")
        self.clear_button = self.findChild(qt_widget.QPushButton, "pushButton_2")

        # Add the value on combo boxes
        # self.combo_box_1.addItems(["option 1", "option 2"])
        # self.combo_box_2.addItems(["option 1", "option 2"])
        self.languages = googles

        # Click the button
        self.trans_button.clicked.connect(self.clear_the_box)
        self.clear_button.clicked.connect(self.translate_text)

        # Show the app window
        self.show()

    # Clear the text Boxes
    def clear_the_box(self):
        pass

    # Translate the text
    def translate_text(self):
        pass

def main():
    # Initialize the App
    app = qt_widget.QApplication(sys.argv)
    window = UI_OpenImage()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()




