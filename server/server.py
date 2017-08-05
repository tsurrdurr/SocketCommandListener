import SocketCreator as creator
import socket
import sys


host = 'localhost'
port = 10000


def main():
    try:
        s = creator.SocketCreator().create(host, port)
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
    main()

