import socket


class Client():
    @staticmethod
    def run():
        connection_served = 0
        s = socket.socket()
        s.connect(('localhost', 10000))
        print("connectionSevered:{0}".format(connection_served))
        while (connection_served == 0):
            try:
                print("Enter message:")
                message = input()
                s.send(message.encode())
            except:
                print('something went wrong')

if __name__ == '__main__':
    Client().run()
