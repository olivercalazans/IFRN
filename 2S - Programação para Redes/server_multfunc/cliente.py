import socket, sys

HOST = 'localhost'
PORT = 50000
CODF = 'utf-8'

# Criando socket.
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conectando ao servidor
conn.connect((HOST, PORT))

while True:
    pedido  = input('>')
    conn.send(pedido.encode(CODF))
    servico = pedido[:2]

    if servico == '/q':
        print('DESLOGADO DO SERVIDOR')
        sys.exit()
    
    if servico == '/l':
        ips = conn.recv(1024).decode(CODF)
        ips = ips.split('/')
        for ip in ips: print(ip)
