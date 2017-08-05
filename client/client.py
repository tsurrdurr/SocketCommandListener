import threading
import socket


class Client():
    def run(self):
        connectionSevered = 0
        s = socket.socket()
        s.connect(('localhost', 10000))
        print("connectionSevered:{0}".format(connectionSevered))
        while (connectionSevered == 0):
            try:
                print("Enter message:")
                response = input()
                print(response)
                s.send(response.encode())
            except:
                print('idk man')

if __name__ == '__main__':
    Client().run()
