import SocketCreator as creator
import socket
import sys

class Server:

    host = 'localhost'
    port = 10000

    def main(self):
        try:
            s = creator.SocketCreator().create(self.host, self.port)
            s.listen(5)
            print('[+] Listening for connections on port')
        except socket.error:
            print('Failed to create socket')
            sys.exit()
        data = ""
        c, addr = s.accept()
        while True:
            data = data + c.recv(1024).decode()
            print(data)
            data = ""

if __name__ == '__main__':
    Server().main()

