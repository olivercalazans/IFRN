import socket, threading, sys, requests, os, datetime, math, time
from chave_api import API_KEY

# ================================= ÁREA DE CONSTANTES ================================================

SMALL_BUFFER = 1024
BIG_BUFFER   = 10240
ALL_CLIENTS  = list()  # Lista de IPs e sockets (tupla).
ATIVIDADE    = list()  # Atividade dos clientes.
LISTA_IPS    = list()  # Lista de IPs.
TRADUCAO     = 'utf-8'
DATA_DE_HOJE = str(datetime.date.today())
NUM_INTERAC  = 10  # Número de interações para escrever no arquivo.
DIRETORIO    = os.path.dirname(os.path.abspath(__file__))
SERVER_FILES = DIRETORIO + '\\server_files\\'
SERVER_HISTO = DIRETORIO + '\\historico\\'

# ================================== ÁREA DE FUNÇÕES ==================================================

# Criação de diretórios.
def escrevendo_historico():
    global ATIVIDADE
    with open(SERVER_HISTO + DATA_DE_HOJE, 'a', encoding=TRADUCAO) as linha:
        for conteudo in ATIVIDADE:
            linha.write(f'{conteudo}\n')
        ATIVIDADE = list()

# BOT do telegram.
def telegram(logg):
    url_req    = f'https://api.telegram.org/bot{API_KEY}'
    requisicao = requests.get(url_req + '/getUpdates')
    retorno    = requisicao.json()
    id_chat    = retorno['result'][0]['message']['chat']['id']
    mensagem   = logg
    resposta   = {'chat_id':id_chat,'text':mensagem}
    envio      = requests.post(url_req + '/sendMessage', data=resposta)

# /?: Lista de comandos.
def lista_comandos(conexao, cliente):
    comandos = ['/l: lista de IPs','/f: Lista de arquivos do servidor','/d: Download de arquivos do servidor',
                '/u: Upload de arquivos para o servidor']
    conexao.send((str(comandos)).encode(TRADUCAO))
    ATIVIDADE.append(f'{str(datetime.datetime.now())}|"/l":{cliente}')
    print(f'{cliente} > "/?"')

# /l: lista de ips.
def lista_ips(conexao, cliente):
    ips = ''
    for ip in LISTA_IPS:
        if ip != cliente:
            ips += f'{ip}/'
    conexao.send(ips.encode(TRADUCAO))
    ATIVIDADE.append(f'{str(datetime.datetime.now())}|"/l":{cliente}')
    print(f'{cliente} > "/l"')

# /f: Lista de arquivos do servidor.
def lista_arquivos(conexao, cliente):
    nomes     = os.listdir(SERVER_FILES)
    full_list = ''
    for nome in nomes:
        full_list += f'{nome}: {os.path.getsize(SERVER_FILES + nome)} bytes/'
    pacotes_f = str(math.ceil(sys.getsizeof(full_list) / SMALL_BUFFER))
    conexao.send(pacotes_f.encode(TRADUCAO))
    conexao.send(full_list.encode(TRADUCAO))
    ATIVIDADE.append(f'{str(datetime.datetime.now())}|"/f":{cliente}')
    print(f'{cliente} > "/f"')

# /d: Download de arquivos do servidor.
def download(conexao, cliente, entrada_comando):
    try: 
        arquivo_d = entrada_comando.split(':')[-1]
        tamanho_d = str(os.path.getsize(SERVER_FILES + arquivo_d))
        conexao.send(tamanho_d.encode(TRADUCAO))
        time.sleep(1)
        with open(SERVER_FILES + arquivo_d, 'rb') as file:
            while True:
                data = file.read(BIG_BUFFER)
                if not data: break
                conexao.send(data)
    except:
        print(f'{cliente}: Envio interrompido!!!')
        ATIVIDADE.append(f'{str(datetime.datetime.now())}|"/d":{cliente}|{arquivo_d}>>{sys.exc_info()[0]}')
    else:
        print(f'{cliente} > "/d" - {arquivo_d}')
        ATIVIDADE.append(f'{str(datetime.datetime.now())}|"/d":{cliente}|{arquivo_d}')

# /u: Upload de arquivos para o servidor.
def upload(conexao, cliente, entrada_comando):
    try:
        arquivo_u = entrada_comando.split(':')[-1]
        print(f'Upload do cliente {cliente} > {arquivo_u}')
        tamanho_u = int((conexao.recv(SMALL_BUFFER)).decode(TRADUCAO))
        if arquivo_u in SERVER_FILES:
            num = 1
            arquivo_u += f'{num}'
            while arquivo_u in SERVER_FILES:
                num2 = num + 1
                arquivo_u.replace(str(num), str(num2))
                num += 1
        with open(SERVER_FILES + arquivo_u, 'wb') as file:
            data_recv = 0
            while data_recv < tamanho_u:
                data = conexao.recv(BIG_BUFFER)
                data_recv += len(data)
                file.write(data)
    except: 
        print(f'\nERRO...:{sys.exc_info()}')
        ATIVIDADE.append(f'{str(datetime.datetime.now())}|"/u":{cliente}|{arquivo_u}>>{sys.exc_info()[0]}')
    else:
        print(f'Upload do cliente {cliente} concluído > {arquivo_u}')
        ATIVIDADE.append(f'{str(datetime.datetime.now())}|"/u":{cliente}|{arquivo_u}')

# Thread onde o cliente faz a interação com o servidor ------------------------------------------
def servicos(conexao, cliente):
    logg = f'Login: {cliente}'
    aviso_in = threading.Thread(target=telegram, args=(logg,))
    aviso_in.start()
    ATIVIDADE.append(f'{str(datetime.datetime.now())}|{logg}')
    print(logg)
    
    while True:
        try: 
            entrada_comando = (conexao.recv(SMALL_BUFFER)).decode(TRADUCAO)
            serv = entrada_comando[:2]

            # Escrevendo histórico de atividades.
            if len(ATIVIDADE) >= NUM_INTERAC: 
                arquivo = threading.Thread(target=escrevendo_historico, args=())
                arquivo.start()
                
            # Lista de comandos.
            if serv == '/?':
                serv_list = threading.Thread(target=lista_comandos, args=(conexao, cliente,))
                serv_list.start()
            
             # Deslogar do servidor.
            elif serv == '/q':
                logg = f'Logout: {cliente}'
                aviso_out = threading.Thread(target=telegram, args=(logg,))
                aviso_out.start()
                ATIVIDADE.append(f'{str(datetime.datetime.now())}|{logg}')
                print(logg)
                ALL_CLIENTS.remove((conexao, cliente))
                break

            # Lista de IPs.
            elif serv == '/l':
                all_ips = threading.Thread(target=lista_ips, args=(conexao, cliente,))
                all_ips.start()
            
            # Lista de arquivos.
            elif serv == '/f':
                files = threading.Thread(target=lista_arquivos, args=(conexao, cliente,))
                files.start()
            
            # Download de arquivos do servidor.
            elif serv == '/d':
                download_file = threading.Thread(target=download, args=(conexao, cliente, entrada_comando,))
                download_file.start()
            
            # Upload de arquivos para o servidor.
            elif serv == '/u':
                upload_file = threading.Thread(target=upload, args=(conexao, cliente, entrada_comando,))
                upload_file.start()
        
        except:
            print(f'O cliente "{cliente}" forçou a desconexão!!!')
            ATIVIDADE.append(f'{str(datetime.datetime.now())}|Logout forçado:{sys.exc_info()[0]}|{cliente}')
            break
        
# =====================================================================================================

# Criando diretório para os históricos.
try:    os.mkdir(SERVER_HISTO)    
except  FileExistsError: print('\nO diretóro já existe.')
except: print(f'\nERRO...:{sys.exc_info()[0]}')
else:   print(f'\nDiretório criado com sucesso!!!') 

# Criando arquivo para fazer os registros.
if not DATA_DE_HOJE in os.listdir(SERVER_HISTO):
    with open(SERVER_HISTO + DATA_DE_HOJE, 'w'): pass
    print('Arquivo criado.')
else: print('O arquivo de hoje já existe.')
    
# Criando socket e escutando a porta.
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', 50000))
    sock.listen(5)
except:
    print(f'\nERRO...:{sys.exc_info()}')
    sys.exit()
else:
    print(f'\nSERVIDOR ATIVO: {sock.getsockname()}')
 
# Recebendo conexão e levando o cliente para uma thread.
try:
    while True:
        conexao, cliente = sock.accept()  # Aceitando conexões.
        thread_cliente = threading.Thread(target=servicos, args=(conexao, cliente,))
        thread_cliente.start()
        ALL_CLIENTS.append((conexao, cliente))
        LISTA_IPS.append(cliente)
except:
    print(f'ERRO...:{sys.exc_info()[0]}')

