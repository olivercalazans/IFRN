import socket, sys, os, time, threading, datetime

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
            recp_data = conn.recv(BIG_BF).decode(TRADUCAO)
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
                else:   print('\nDownload concluído.')
            
            # Download da web (APENAS AVISOS DE ERRO).
            elif recp_data[0] == 'w':
                if recp_data[1] == '0':
                    print(recp_data[2:])
                else:
                    try:
                        nome_arq = recp_data[3:]
                        print(f'Baixando arquivo: {nome_arq}')
                        tamanho_dw = int(conn.recv(SMALL_BF))
                        dados_recv_dw   = 0
                        with open(CLIENT_FL + nome_arq, 'wb') as linha:
                            while dados_recv_dw < tamanho_dw:
                                data_dw = conn.recv(BIG_BF)
                                linha.write(data_dw)
                                dados_recv_dw += len(data_dw)
                    except: print(f'ERRO...:{sys.exc_info()}')
                    else:   print('\nDownload concluído.')
            
            # RSS.
            elif recp_data[0] == 'r':
                while True:
                    urls = conn.recv(BIG_BF).decode(TRADUCAO)
                    if len(urls) > 0: break
                urls = urls.split('<+>')
                for url in urls:
                    print(url)


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
    
    # Aviso para a função de download da web.
    elif pedido[:2] == '/w':
        print('Aguarde um momento, isso pode levar alguns minutos.')
    
    # Upload de arquivos para o servidor.
    elif pedido[:2] == '/u':
        nome_arq_u = pedido[3:]
        print(f'Enviando arquivo: {nome_arq_u}')
        try:
            tamanho_u = str(os.path.getsize(CLIENT_FL + nome_arq_u))
            conn.send(tamanho_u.encode(TRADUCAO))
            while True:
                sys.stdout.write(f'\r{datetime.datetime.now()}')
                sys.stdout.flush()
                confirmacao = conn.recv(SMALL_BF).decode(TRADUCAO)
                if confirmacao == 'SEND_OK':
                    with open(CLIENT_FL + nome_arq_u, 'rb') as file:
                        while True:
                            data_u = file.read(BIG_BF)
                            if not data_u: break
                            conn.send(data_u)
                        break
        except FileNotFoundError: print(f'Arquivo não encontrado: {nome_arq_u}')
        except: print(f'Erro...:{sys.exc_info()}')    
        else:   print('Arquivo enviado com sucesso.')
