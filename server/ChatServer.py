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


if __name__ == '__main__':
    server = ChatServer()
