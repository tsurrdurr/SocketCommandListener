import threading
import socket
import sys
host = 'localhost'
port = 10000

class connectionThread(threading.Thread):
    def __init__(self, host, port):
        super(connectionThread, self).__init__()
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.bind((host,port))
            self.s.listen(5)
        except socket.error:
            print('Failed to create socket')
            sys.exit()
        self.clients = []

    def run(self):
        while True:
            conn, address = self.s.accept()
            c = client(conn)
            c.start()
            c.send_msg(u"\r\n")
            self.clients.append(c)
            print('[+] Client connected: {0}'.format(address[0]))


def main():
    get_connections = connectionThread(host, port)
    get_connections.start();
    while True:
        try:
            response = 'got something'
            for c in get_connections.clients:
                c.send_msg(response)
        except KeyboardInterrupt:
            sys.exit()

if __name__ == '__main__':
    main()

