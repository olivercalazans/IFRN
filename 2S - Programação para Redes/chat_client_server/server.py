import socket, threading

class Server:
    def __init__(self):
        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server_socket.bind(('localhost', 50000))
        self._server_socket.listen(4)
        print(f'\nSERVIDOR ATIVO: {self._server_socket.getsockname()}')
        self._connection     = None
        self._client_address = None

    def receiving_client(self):
        while True:
            self._connection, self._client_address = self._server_socket.accept()
            print(f'New log in: {self._client_address}')
            threading.Thread(target=self.handle_client).start()

    def handle_client(self):
        while True:  
                message = self._connection.recv(1024).decode()
                if message:
                    if message  == 'EXIT': 
                        self.logging_out()
                        break
                    print(f'{self._client_address}> {message}')
                #else: break

    def logging_out(self):
        self._connection.close()

if __name__ == '__main__':
    server = Server()
    server.receiving_client()