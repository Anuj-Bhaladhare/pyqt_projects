# Creating the Vertual Envoirment in Python for the PyQt

1.  pip install virtualenv 
2.  python -m venv myenv
3.  myenv\Scripts\activate  -> [for Activat env]
4.  deactivate              -> [for DeActivat env]



C:\Users\anujb\AppData\Local\Programs\Python\Python312\Scripts
pyuic5 buttonTest.ui -o buttonexample.py 
{pyuic5 ../../buttonTest.ui -o buttonexample.py}    --> Command is Working


this also the working command :-> myenv\Scripts\pyuic5 source_file.ui -o result_file.py












# ================>> Template GUI <<================

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton


class UI(QWidget):
    def __init__(self):
        super().__init__()


app = QApplication([])
window = UI()
window.show()
app.exec_()


