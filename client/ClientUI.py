import sys

from PyQt5.QtWidgets import QApplication

from client.LoginView import LoginView


class ClientUI:
    def __init__(self, controller):
        self.app = QApplication(sys.argv)
        self.login_view = LoginView(controller)
        self.login_view.show()

    def start(self):
        sys.exit(self.app.exec_())
