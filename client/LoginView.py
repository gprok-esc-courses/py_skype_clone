from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QLabel, QLineEdit, QWidget, QPushButton
import sys


class LoginView:
    def __init__(self, controller):
        self.controller = controller
        self.window = QWidget()
        self.window.setGeometry(300, 300, 300, 120)
        self.window.setWindowTitle("PySkype Login")
        layout = QGridLayout()

        username_label = QLabel('Username:')
        self.username_field = QLineEdit()
        layout.addWidget(username_label, 0, 0)
        layout.addWidget(self.username_field, 0, 1)

        password_label = QLabel('Password:')
        self.password_field = QLineEdit()
        self.password_field.setEchoMode(QLineEdit.Password)
        layout.addWidget(password_label, 1, 0)
        layout.addWidget(self.password_field, 1, 1)

        login_button = QPushButton('Login')
        login_button.clicked.connect(self.login_btn_clicked)
        layout.addWidget(password_label, 1, 0)
        layout.addWidget(login_button, 2, 0, 1, 2)

        self.window.setLayout(layout)
        # EXERCISE 2: Add a label LOGIN, fields for Username and Password, and a Login Button

    def login_btn_clicked(self):
        self.controller.login(self.username_field.text(), self.password_field.text())

    def show(self):
        self.window.show()

