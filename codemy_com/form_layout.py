import PyQt5.QtWidgets as qt_widget
import PyQt5.QtGui as qt_gui
import sys

class Form_Layout_UI(qt_widget.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Form Layout")
        self.form_layout = qt_widget.QFormLayout()
        self.setLayout(self.form_layout)   # Changed Here [QFormLayout()]

        self.label = qt_widget.QLabel()
        self.label.setText("this is the label text")
        self.layout().addWidget(self.label)

        # Add Stuff/Widgets
        self.lable_1 = qt_widget.QLabel()
        self.lable_1.setText("Add Your First Name and Last Name")
        self.lable_1.setFont(qt_gui.QFont('Helvetica', 24))
        self.layout().addWidget(self.lable_1)

        self.f_name = qt_widget.QLineEdit(self)
        self.l_name = qt_widget.QLineEdit(self)

        # Add Lable 2
        self.lable_2 = qt_widget.QLabel()
        self.lable_2.setText("Not Selected")
        
        # Add Button in the Form
        self.button = qt_widget.QPushButton()
        self.button.setText("Clicked Me!")
        self.button.clicked.connect(self.pressed_button)

        # Add Rows To App
        self.form_layout.addRow(self.lable_1)
        self.form_layout.addRow("First Name: ", self.f_name)
        self.form_layout.addRow("Last Name: ", self.l_name)
        self.form_layout.addRow(self.layout().addWidget(self.button))
        self.form_layout.addRow("Full Name: ", self.layout().addWidget(self.lable_2))
 
        self.show()
        
    def pressed_button(self):
        print("Button is Pressed")
        self.lable_2.setText(f"{self.f_name.text()} {self.l_name.text()}")
        

app = qt_widget.QApplication([])
q_mw = Form_Layout_UI()
app.exec_()

