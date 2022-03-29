import os
from socket import socket, AF_INET, SOCK_STREAM

import rsa
# from Crypto.PublicKey import RSA

from client.ClientUI import ClientUI
from client.LoginView import LoginView
from server.EncryptionManager import EncryptionManager


class ChatClient:
    def __init__(self):
        current_dir = os.path.dirname(__file__)
        self.encryption = EncryptionManager(current_dir)
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(('127.0.0.1', 8005))
        # Wait for public key
        # self.server_public_key = RSA.importKey(self.client_socket.recv(1024), passphrase=None)
        # print(self.server_public_key)
        self.ui = ClientUI(self)
        self.ui.start()

    def login(self, username, password):
        print("DATA RECEIVED: " + username + password)
        data = '{"username": "' + username + '", "password": "' + password + '"}'
        self.client_socket.send(str.encode(data))
        # send login data to the server
        # Get response
        # If response is OK close Login Form and display Skype form
        # else display error message


if __name__ == '__main__':
    client = ChatClient()
