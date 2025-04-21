import PyQt5.QtWidgets as qt_widget
import PyQt5.QtGui as qt_gui
import sys

class Text_Boxex_UI(qt_widget.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Text Boxex Window")
        self.setGeometry(200, 200, 500, 500)
        self.setLayout(qt_widget.QVBoxLayout())

        self.label = qt_widget.QLabel()
        self.label.setText("This is the lable text")
        self.label.setFont(qt_gui.QFont('Helvetica', 20))
        self.layout().addWidget(self.label)

        self.text_box = qt_widget.QTextEdit(self,
            html = "<h1>this is the HTML tag</h1>",
            acceptRichText = False,
            lineWrapMode = qt_widget.QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth = 10,
            placeholderText = "Hello World!",
            readOnly = False,                   
            )
        self.layout().addWidget(self.text_box)

        self.my_button = qt_widget.QPushButton()
        self.my_button.setText("Click Me!")
        self.my_button.clicked.connect(self.pressed_it)
        self.layout().addWidget(self.my_button)

        self.show()

    
    def pressed_it(self):
        print("this button is pressed")
        self.label.setText(f"Your Text: {self.text_box.toPlainText()}!")

app = qt_widget.QApplication([])
win = Text_Boxex_UI()
app.exec_()
