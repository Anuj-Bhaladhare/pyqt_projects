import PyQt5.QtWidgets as qt_widgets
import PyQt5.QtGui as qt_gui
import sys

class SpinnBox_UI(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Sppin Box")
        self.setGeometry(200, 200, 200, 200)
        self.setLayout(qt_widgets.QVBoxLayout())

        self.label = qt_widgets.QLabel()
        self.label.setText("Pick Something from Option")

        # Change the font size for label
        self.label.setFont(qt_gui.QFont('Helvetica', 24))
        self.layout().addWidget(self.label)

        # Create an Spin box
        self.my_spin = qt_widgets.QSpinBox(self, 
            value = 10,
            maximum = 100,
            minimum = 0,
            singleStep = 7.50,
            prefix = "#",  # Add value in Front
            suffix = " Order")  # Add value in Back
        
        self.my_button = qt_widgets.QPushButton()
        self.my_button.setText("Press Me!")
        self.my_button.clicked.connect(self.button_clicked)
        self.layout().addWidget(self.my_button)
        # Change font size of Spinn Box
        self.my_spin.setFont(qt_gui.QFont('Helvetica', 18))

        self.layout().addWidget(self.my_spin)
        self.show()

    def button_clicked(self):
        self.label.setText(f"You Have Selected the Value: {self.my_spin.value()}")
        print("This is the value")


app = qt_widgets.QApplication([])
win = SpinnBox_UI()
app.exec_()


