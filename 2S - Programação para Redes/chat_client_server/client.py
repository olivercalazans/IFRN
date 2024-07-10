import socket

class Client:
    def __init__(self, ip='localhost', port=50000):
        self._connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._connection.connect((ip, port))

    def sending_messages(self):
        while True:
            message = input('>')
            self._connection.sendall(message.encode())
            if message == 'EXIT': 
                break

    def closing_connection(self):
        self._connection.close()

if __name__ == '__main__':
    client = Client()
    client.sending_messages()
    client.closing_connection()
