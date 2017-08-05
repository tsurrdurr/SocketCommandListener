import socket


class SocketCreator:
    s = socket.socket()
    default_host = 'localhost'
    default_port = 10000

    def create(self, host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))
        return s