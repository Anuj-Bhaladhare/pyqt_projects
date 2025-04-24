import PyQt5.QtWidgets as qt_widget
import PyQt5.QtGui as qt_gui
from views.main_window_view import MainWindowView
import sys

def main():
    app = qt_widget.QApplication(sys.argv)
    window = MainWindowView()  # Load the Main UI
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

    