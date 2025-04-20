import PyQt5.QtWidgets as qt_widgets
import PyQt5.QtGui as qt_gui
import sys

class Combo_Box(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        
        # Add the Title
        self.setWindowTitle("Combo box Title")

        #Add the Verticle Layout
        self.setLayout(qt_widgets.QVBoxLayout())

        # Create the Lable
        self.my_label = qt_widgets.QLabel()
        self.my_label.setText("this is the lable")
        self.layout().addWidget(self.my_label)

        # Create a Combo Box
        self.my_combo = qt_widgets.QComboBox(self)
        # Add Item to Combe Box
        self.my_combo.addItems(["Option 1", "Option 2", "Option 3", "Option 4"])
        self.layout().addWidget(self.my_combo)

        # Create the Button
        my_btn = qt_widgets.QPushButton()
        my_btn.setText("Click Me!")
        my_btn.clicked.connect(self.clicked_option)
        self.layout().addWidget(my_btn)

        self.show()

    def clicked_option(self):
        selected = self.my_combo.currentText()
        self.my_label.setText(f"You Have Clicked {selected}")
        print("Button is Clicked...")
        


app = qt_widgets.QApplication([])
mw = Combo_Box()

app.exec_()

