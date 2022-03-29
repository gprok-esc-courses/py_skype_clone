import json
import os
from socket import socket, AF_INET, SOCK_STREAM

from server.DBConnection import DBConnection
from server.EncryptionManager import EncryptionManager


class ChatServer:
    def __init__(self):
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.bind(('127.0.0.1', 8005))
        self.server_socket.listen()
        current_dir = os.path.dirname(__file__)
        self.encryption = EncryptionManager(current_dir)
        self.db = DBConnection()
        self.start_server()

    def start_server(self):
        while True:
            print("Waiting for connection ...")
            conn, addr = self.server_socket.accept()
            print(conn)
            # send server's public key
            # conn.send(self.encryption.public_key.exportKey(format='PEM', passphrase=None, pkcs=1))
            login_data = conn.recv(1024).decode('utf-8')
            print(login_data)
            login_json = json.loads(login_data)
            print("Username: " + login_json['username'])
            print("Password: " + login_json['password'])
            # EXERCISE: Check if username and password are in database and respond to client


if __name__ == '__main__':
    server = ChatServer()
