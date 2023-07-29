import socket, sys, os, time, threading

# lista de arquivos

# ================================ ÁREA DE CONSTANTES ==================================
SMALL_BF  = 1024
BIG_BF    = 10240
HOST      = 'localhost'
PORT      = 50000
TRADUCAO  = 'utf-8'
DIRETORIO = os.path.dirname(os.path.abspath(__file__))
CLIENT_FL = DIRETORIO + '\\client_file\\'
# ================================ RECEPTOR DE DADOS ===================================

def receptor():
        global runnig
        while runnig:
            recp_data = conn.recv(SMALL_BF).decode(TRADUCAO)
            data = recp_data[2:]
            if recp_data[0] == '?':
                comandos = eval(recp_data[2:])
                for comando in comandos: print(comando)

            # Lista de IPs.
            elif recp_data[0] == 'l':
                ips = recp_data[2:].split('/')
                for ip in ips: print(ip)
            
            # Mensagens privadas/broadcast.
            elif recp_data[0] == 'm':
                print(recp_data[2:])
            
            # Históico de mensagens.
            elif recp_data[0] == 'h':
                msg_h = recp_data[2:]
                if msg_h == '0':
                    print('Você ainda não enviou mensagens.')
                else:
                    msg_h = eval(msg_h)
                    for linha in msg_h:
                        print(f'{linha[0]} |> {linha[1]}: {linha[2]}')

            # Lista de arquivos.
            elif recp_data[0] == 'f':
                pacotes_f = int(recp_data[2:])
                arquivos  = ''
                for loop in range(pacotes_f): arquivos += conn.recv(SMALL_BF).decode(TRADUCAO)
                arquivos = arquivos.split('/')
                for arquivo in arquivos: print(arquivo)

            # Downoad de arquivos do servidor.
            elif recp_data[0] == 'd':
                try:
                    arquivo_d = pedido.split(':')[-1]
                    print(f'Baixando arquivo: {arquivo_d}')
                    tamanho_arq = int(conn.recv(SMALL_BF).decode(TRADUCAO))
                    dados_recv  = 0
                    with open(CLIENT_FL + arquivo_d, 'wb') as file:
                        while dados_recv < tamanho_arq:
                            data = conn.recv(BIG_BF)
                            file.write(data)
                            dados_recv += len(data)
                            sys.stdout.write(f'\rBytes recebidos: {dados_recv}/{tamanho_arq}')
                            sys.stdout.flush()
                except: print(f'ERRO...:{sys.exc_info()}')
                else: print('\nDownload concluído.')

# =======================================================================================

# Criando socket e conectando ao servidor.
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((HOST, PORT))

# Criando arquivo para o cliente.
try:    os.mkdir(CLIENT_FL)    
except  FileExistsError: print('\nO diretório já existe.')
except: print(f'\nERRO...:{sys.exc_info()[0]}')
else:   print(f'\nDiretório criado com sucesso!!!') 

# Ativando receptor.
runnig = True
tRECEPTOR = threading.Thread(target=receptor)
tRECEPTOR.start()

# Envio de comandos.
while True:
    pedido = input('\n>')
    conn.send(pedido.encode(TRADUCAO))
    time.sleep(0.3)

    # Sair do servidor.
    if pedido [:2] == '/q':
        runnig = False
        print('\nDESLOGADO DO SERVIDOR')
        sys.exit()
        
