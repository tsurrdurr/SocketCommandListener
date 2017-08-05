import socket
from multipledispatch import dispatch

default_host = 'localhost'
default_port = 10000


class SocketCreator:
    s = socket.socket()

    def create(self, host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))
        return s