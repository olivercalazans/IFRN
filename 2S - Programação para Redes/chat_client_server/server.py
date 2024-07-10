import socket, threading

class Server:
    def __init__(self):
        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server_socket.bind(('localhost', 50000))
        self._server_socket.listen(4)
        print(f'\nSERVIDOR ATIVO: {self._server_socket.getsockname()}')
        self._clients_list   = dict()
        self._lock           = threading.Lock()

    def receiving_client(self):
        while True:
            connection, client_address = self._server_socket.accept()
            print(f'New log in: {client_address}')
            threading.Thread(target=self.handle_client, args=(connection, client_address,)).start()

    def add_client_to_the_list(self, connection, client_address):
        with self._lock:
            self._clients_list[client_address] = connection

    def remove_client_from_the_list(self, connection, client_address):
        with self._lock:
            connection.close()
            del self._clients_list[client_address]

    def handle_client(self, connection, client_address):
        self.add_client_to_the_list(connection, client_address)
        while True:
            try:
                message = connection.recv(1024).decode()
                if message:
                    if message  == 'EXIT': 
                        self.remove_client_from_the_list(connection, client_address)
                        break
                    print(f'{client_address[1]}> {message}')
                else: break
            except Exception as error:
                print(error)
                self.remove_client_from_the_list(connection, client_address)


if __name__ == '__main__':
    server = Server()
    server.receiving_client()
