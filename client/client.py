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
                message = input()
                s.send(message.encode())
            except:
                print('something went wrong')

if __name__ == '__main__':
    Client().run()
