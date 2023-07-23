import socket, sys, os

# ===================================================
SMALL_BF  = 1024
BIG_BF    = 10240
HOST      = 'localhost'
PORT      = 50000
TRADUCAO  = 'utf-8'
DIRETORIO = os.path.dirname(os.path.abspath(__file__))
CLIENT_FL = DIRETORIO + '\\client_file\\'
# ===================================================

try:    os.mkdir(CLIENT_FL)    
except  FileExistsError: print('\nO diretóro já existe.')
except: print(f'\nERRO...:{sys.exc_info()[0]}')
else:   print(f'\nDiretório criado com sucesso!!!') 

# Criando socket.
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conectando ao servidor
conn.connect((HOST, PORT))

while True:
    pedido  = input('>')
    conn.send(pedido.encode(TRADUCAO))
    servico = pedido[:2]

    # Sair do servidor.
    if servico == '/q':
        print('DESLOGADO DO SERVIDOR')
        sys.exit()
    
    # Lista de IPs.
    elif servico == '/l':
        ips = conn.recv(SMALL_BF).decode(TRADUCAO)
        ips = ips.split('/')
        for ip in ips: print(ip)
    
    # Lista de arquivos do servidor.
    elif servico == '/f':
        pacotes_f = int(conn.recv(SMALL_BF).decode(TRADUCAO))
        arquivos  = ''
        for loop in range(pacotes_f): arquivos += conn.recv(SMALL_BF).decode(TRADUCAO)
        arquivos = arquivos.split('/')
        for arquivo in arquivos: print(arquivo)
    
    elif servico == '/d':
        tamanho_arq = int(conn.recv(SMALL_BF))
        dados_recv  = 0
        with open(CLIENT_FL + pedido.split(':')[-1], 'wb') as file:
            while dados_recv < tamanho_arq:
                data = conn.recv(BIG_BF)
                file.write(data)
                dados_recv += len(data)
                sys.stdout.write(f'\r {dados_recv}/{tamanho_arq} bytes recebidos')
                sys.stdout.flush()
