import os
from socket import socket, AF_INET, SOCK_STREAM

from client.LoginView import LoginView
from server.EncryptionManager import EncryptionManager


class ChatClient:
    def __init__(self):
        current_dir = os.path.dirname(__file__)
        self.encryption = EncryptionManager(current_dir)
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(('127.0.0.1', 8005))
        self.login_view = LoginView()
        self.login_view.show()


if __name__ == '__main__':
    client = ChatClient()