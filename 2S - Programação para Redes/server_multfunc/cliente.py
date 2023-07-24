import socket, sys, os, threading, time

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
except  FileExistsError: print('\nO diretório já existe.')
except: print(f'\nERRO...:{sys.exc_info()[0]}')
else:   print(f'\nDiretório criado com sucesso!!!') 

# Criando socket.
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conectando ao servidor.
conn.connect((HOST, PORT))

while True:
    pedido  = input('>')
    conn.send(pedido.encode(TRADUCAO))
    servico = pedido[:2]

    # Lista de comandos.
    if servico == '/?':
        comandos = eval((conn.recv(SMALL_BF)).decode(TRADUCAO))
        for comando in comandos: print(comando)

    # Sair do servidor.
    elif servico == '/q':
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
    # Download de arquivos.
    elif servico == '/d':
        def download_file():
            try:
                print('Baixando arquivo...')
                tamanho_arq = int(conn.recv(SMALL_BF).decode(TRADUCAO))
                dados_recv  = 0
                with open(CLIENT_FL + pedido.split(':')[-1], 'wb') as file:
                    while dados_recv < tamanho_arq:
                        data = conn.recv(BIG_BF)
                        file.write(data)
                        dados_recv += len(data)
            except: print(f'\nERRO...:{sys.exc_info()}')
            else: print('Download concluído.')
                
        if pedido.split(':')[-1] in os.listdir(CLIENT_FL):
            print(f'O arquivo "{pedido.split(":")[-1]}" já existe.')
        else:
            tDOWNLOAD = threading.Thread(target=download_file)
            tDOWNLOAD.start()
    
    elif servico == '/u':
        def upload_file():
            try:
                file_path = CLIENT_FL + pedido.split(':')[-1]
                tamanho_u = str(os.path.getsize(file_path))
                conn.send(((tamanho_u).encode(TRADUCAO)))
                time.sleep(2)
                while True:
                    with open(file_path, 'rb') as file:
                        data = file.read(BIG_BF)
                        if not data: break
                        conn.send(data)
            except: print(f'\nERRO...:{sys.exc_info()}')
            else: print(f'Upload concluído: {pedido.split(":")[-1]}')
        tUPLOAD = threading.Thread(target=upload_file)
        tUPLOAD.start()
