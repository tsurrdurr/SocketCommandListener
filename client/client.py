import threading
import socket

class client(threading.Thread):
    def __init__(self, conn):
        super(client, self).__init__()
        self.conn = conn
        self.data = ""

    def run(self):
        while True:
            self.data = self.data + self.conn.recv(1024)
            if self.data.endswith(u"\r\n"):
                print(self.data)
                self.data = ""

    def send_msg(self,msg):
        self.conn.send(msg)

    def close(self):
        self.conn.close()


cl = client()