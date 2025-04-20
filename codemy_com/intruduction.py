import PyQt5.QtWidgets as qt_widgets
import PyQt5.QtGui as qt_gui

class MainWindow(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        # Add window Title
        self.setWindowTitle("Hello World!!")

        # Set Layout
        self.setLayout(qt_widgets.QVBoxLayout())

        # Create the Label
        my_lable = qt_widgets.QLabel("this is the label")
        # change the font and text size
        my_lable.setFont(qt_gui.QFont('Helvetica', 18))
        self.layout().addWidget(my_lable)

        # Create an entry box
        my_entry = qt_widgets.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("")
        self.layout().addWidget(my_entry)

        # Create the button
        btn = qt_widgets.QPushButton()
        btn.setText("Click Me!")
        btn.clicked.connect(lambda: prrss_it())
        self.layout().addWidget(btn)

        self.show()

        def prrss_it(self):
            # Add name to label
            print(f"Hello {my_entry.text()}")
            # Clear the entry box
            my_entry.setText("")


app = qt_widgets.QApplication([])
mw = MainWindow()

# Run The App
app.exec_()