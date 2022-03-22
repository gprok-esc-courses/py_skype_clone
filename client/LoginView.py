from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class LoginView:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.window.setGeometry(300, 300, 300, 300)
        self.window.setWindowTitle("PySkype")
        # EXERCISE 2: Add a label LOGIN, fields for Username and Password, and a Login Button

    def show(self):
        self.window.show()
        sys.exit(self.app.exec_())

