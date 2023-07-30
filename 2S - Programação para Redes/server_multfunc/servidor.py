import socket, threading, sys, requests, os, datetime, math, ssl
from chave_api import API_KEY

# verificador de repetição das fotos
# erro ao sair abruptamente, lista de ips

# ================================= ÁREA DE CONSTANTES ================================================

SMALL_BUFFER = 1024
BIG_BUFFER   = 10240
ALL_CLIENTS  = list()  # Lista de IPs e sockets (tupla).
ATIVIDADE    = list()  # Atividade dos clientes.
MENSAGENS    = list()
TRADUCAO     = 'utf-8'
DATA_DE_HOJE = str(datetime.date.today())
NUM_INTERAC  = 5  # Número de interações para escrever no arquivo.
DIRETORIO    = os.path.dirname(os.path.abspath(__file__))
SERVER_FILES = DIRETORIO + '\\server_files\\'
SERVER_HISTO = DIRETORIO + '\\historico\\'

# ================================== ÁREA DE FUNÇÕES ==================================================

# Escrevendo histório.
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

# Verificador de repetição de nome.
def repeticao(name_img):
    nome, tipo = os.path.splitext(name_img)
    lis = os.listdir(DIRETORIO)
    contador = 1
    while True:
        name_img = nome + f'({contador})' + tipo
        if not name_img in lis: break
        contador += 1
        name_img = ''
    return name_img

# /?: Lista de comandos.
def lista_comandos(conexao, cliente):
    comandos = ['/l: lista de IPs','/f: Arquivos do servidor','/m: mensagem privada','/b: mensagem broadcast'
                ,'/d: Download do servidor']
    conexao.send(('?:' + str(comandos)).encode(TRADUCAO))
    ATIVIDADE.append(f'{str(datetime.datetime.now())}|"/l":{cliente}')
    print(f'{cliente} > "/?"')

# /l: lista de ips.
def lista_ips(conexao, cliente):
    mensagem_l = ''
    if len(ALL_CLIENTS) == 1:
        mensagem_l = 'Você é o único logado no servidor.'
    else:
        for ip in ALL_CLIENTS:
            if ip[1] != cliente:
                mensagem_l += f'{ip[1]}/'
        
    conexao.send(('l:' + mensagem_l).encode(TRADUCAO))
    ATIVIDADE.append(f'{str(datetime.datetime.now())}|"/l":{cliente}')
    print(f'{cliente} > "/l"')

# /f: Lista de arquivos do servidor.
def lista_arquivos(conexao, cliente):
    nomes     = os.listdir(SERVER_FILES)
    full_list = ''
    for nome in nomes:
        full_list += f'{nome}: {os.path.getsize(SERVER_FILES + nome)} bytes/'
    pacotes_f = str(math.ceil(sys.getsizeof(full_list) / SMALL_BUFFER))
    conexao.send(('f:' + pacotes_f).encode(TRADUCAO))
    conexao.send(full_list.encode(TRADUCAO))
    ATIVIDADE.append(f'{str(datetime.datetime.now())}|"/f":{cliente}')
    print(f'{cliente} > "/f"')

# /m: Mensagem/chat
def chat_mensagem(conexao, cliente, entrada_comando):
    porta_c    = entrada_comando.split(':')[1]
    mensagem_c = entrada_comando.split(':')[2]
    for addr in ALL_CLIENTS:
        if porta_c == str(addr[1][1]):
            conn, msg, aviso = addr[0], str(cliente[1]) + ': ' + mensagem_c, 'enviada'
            break
    else:
        conn, msg, aviso = conexao, 'Cliente offline, mensagem não enviada', 'não enviada'
    
    conn.send(('m:' + msg).encode(TRADUCAO))
    ATIVIDADE.append(f'{str(datetime.datetime.now())}|"/m":{cliente}|{aviso}|{mensagem_c}')
    MENSAGENS.append([cliente[1],porta_c,mensagem_c])

# /b: Mensagem em broadcast.
def broadcast(conexao, cliente, entrada_comando):
    mensagem_b = entrada_comando.split(':')[1]
    if len(ALL_CLIENTS) == 1:
        conexao.send('m:Mensagem não enviada. Você é o único logado.'.encode(TRADUCAO))
        ATIVIDADE.append(f'{str(datetime.datetime.now())}|"/b":{cliente}|{"não enviada, único logado"}|{mensagem_b}')
    else:
        for dados_con in ALL_CLIENTS:
            if not cliente == dados_con[1]:
                dados_con[0].send((f'm:{cliente[1]}(broad):{mensagem_b}').encode(TRADUCAO))
        ATIVIDADE.append(f'{str(datetime.datetime.now())}|"/b":{cliente}|{mensagem_b}')
        MENSAGENS.append([cliente[1],'(broad)',mensagem_b])
    
# /h: Histório de mensagens.
def historico(conexao, cliente):
    mensagens_h = list(filter(lambda c: c[0] == cliente[1], MENSAGENS))
    if len(mensagens_h) > 0:
        conexao.send(('h:' + str(mensagens_h)).encode(TRADUCAO))
    else:
        conexao.send('h:0'.encode(TRADUCAO))

# /d: Download de arquivos do servidor.
def download(conexao, cliente, entrada_comando):
    try: 
        conexao.send('d'.encode(TRADUCAO))
        arquivo_d = entrada_comando.split(':')[-1]
        tamanho_d = str(os.path.getsize(SERVER_FILES + arquivo_d))
        conexao.send(tamanho_d.encode(TRADUCAO))
        with open(SERVER_FILES + arquivo_d, 'rb') as file:
            while True:
                data = file.read(BIG_BUFFER)
                if not data: break
                conexao.send(data)
    except:
        print(f'{cliente}: Envio interrompido > {sys.exc_info()[0]}')
        ATIVIDADE.append(f'{str(datetime.datetime.now())}|"/d":{cliente}|{arquivo_d}>>{sys.exc_info()[0]}')
    else:
        print(f'{cliente} > "/d" - {arquivo_d}')
        ATIVIDADE.append(f'{str(datetime.datetime.now())}|"/d":{cliente}|{arquivo_d}')

# /w: Download da web.
def web_download(conexao, cliente, entrada_comando): 
    try:
        url  = entrada_comando[3:]
        aux1 = url.find('//')           # Auxiliar de procura 1.
        url1 = url[aux1 + 2:]           # URL sem o protocolo e //.
        aux2 = url1.find('/')           # Auxiliar de procura 2.

        # Dados extraídos da URL.
        protocol  = url.split(':')[0]   # Protocolo.
        url_image = url1[aux2:]         # Caminho e nome da imagem.
        url_host  = url1.split('/')[0]  # Nome do host.
        name_img  = url1.split('/')[-1]
        name_img  = name_img.split('.')[0]
        
        url_request = f'GET {url_image} HTTP/1.1\r\nHOST: {url_host}\r\nConnection:close\r\n\r\n'
        sock_img = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                
                # Verificando o protocolo.
        if protocol != 'http' and protocol != 'https':
            print('protocolo errado.')
            #conexao.send((f'w:Download penas de imagens com os protocolos HTTP ou HTTPS. Protocolo: {protocol}').encode(TRADUCAO))
        else:
            if protocol == 'http':
                host_port   = 80
                sock_img.connect((url_host, host_port))
                sock_img.sendall(url_request.encode())
            elif protocol == 'https':
                host_port = 443
                context   = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode    = ssl.CERT_NONE
                socket_rss = socket.create_connection((url_host, host_port))
                sock_img   = context.wrap_socket(socket_rss, server_hostname=url_host)
                sock_img.send(url_request.encode())

        print('Baixando a imagem...')
        # Montado a variável que armazenará os dados de retorno
        data_ret = ''.encode()
        while True:
            data = sock_img.recv(1024)
            if not data: break
            data_ret += data

        # Obtendo o tamanho da imagem e o tipo de aquivo.
        type_name = ''
        tmp = data_ret.split('\r\n'.encode())
        for line in tmp:
            # Tipo de arquivo.
            if 'Content-Type:'.encode() in line:
                type_name = str(line.split()[1])
                break

        # Dados que serão usados.
        type_name  = type_name.split('/')[1]
        type_name  = type_name.replace("'","")
        name_img += f'.{type_name}'

        # Separando o Cabeçalho dos Dados
        delimiter = '\r\n\r\n'.encode()
        position  = data_ret.find(delimiter)
        image     = data_ret[position + 4:]

        # Verificando repetição de nomes.
        name_img = repeticao(name_img)

        # Salvando a imagem
        file_output = open(SERVER_FILES + f'{name_img}', 'wb')
        file_output.write(image)
        file_output.close()

        try:
            conexao.send((f'w1:{name_img}').encode(TRADUCAO))
            tamanho_d = str(os.path.getsize(SERVER_FILES + name_img))
            conexao.send(tamanho_d.encode(TRADUCAO))
            with open(SERVER_FILES + name_img, 'rb') as file:
                while True:
                    data = file.read(BIG_BUFFER)
                    if not data: break
                    conexao.send(data)
        except:
            print(f'{cliente}: Envio interrompido > {sys.exc_info()[0]}')
            ATIVIDADE.append(f'{str(datetime.datetime.now())}|"/w":{cliente}|{name_img}>>{sys.exc_info()[0]}')
        else:
            print(f'{cliente} > "/w" - {name_img}')
            ATIVIDADE.append(f'{str(datetime.datetime.now())}|"/w":{cliente}|{name_img}')
    except:
        print(f'Erro ao baixar o arquivo {name_img}: {sys.exc_info()}')
        conexao.send((str(f'w:Erro ao baixar o arquivo {name_img}: {sys.exc_info()[0]}')).encode(TRADUCAO))
        ATIVIDADE.append(f'{str(datetime.datetime.now())}|"/w":{cliente}|{name_img}|ERRO:{sys.exc_info()[0]}|{url}')

# ============================== Thread onde o cliente faz a interação com o servidor =====================================

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
                tHISTORICO = threading.Thread(target=escrevendo_historico, args=())
                tHISTORICO.start()
            
            
            # Deslogar do servidor.
            if serv == '/q':
                logg = f'Logout: {cliente}'
                aviso_out = threading.Thread(target=telegram, args=(logg,))
                aviso_out.start()
                ATIVIDADE.append(f'{str(datetime.datetime.now())}|{logg}')
                print(logg)
                ALL_CLIENTS.remove((conexao, cliente))
                break
            
            # Lista de comandos.
            elif serv == '/?':
                tSERVER_LIST = threading.Thread(target=lista_comandos, args=(conexao, cliente,))
                tSERVER_LIST.start()

            # Lista de IPs.
            elif serv == '/l':
                tIPS = threading.Thread(target=lista_ips, args=(conexao, cliente,))
                tIPS.start()
            
            # Mensagens privadas.
            elif serv == '/m':
                tCHAT = threading.Thread(target=chat_mensagem, args=(conexao, cliente, entrada_comando,))
                tCHAT.start()
            
            # Mensagem em broadcast.
            elif serv == '/b':
                tBROADCAST = threading.Thread(target=broadcast, args=(conexao, cliente, entrada_comando,))
                tBROADCAST.start()
            
            # Histórico de mensagens.
            elif serv == '/h':
                tHISTORICO = threading.Thread(target=historico, args=(conexao, cliente,))
                tHISTORICO.start()
            
            # Lista de arquivos.
            elif serv == '/f':
                tFILES = threading.Thread(target=lista_arquivos, args=(conexao, cliente,))
                tFILES.start()
            
            # Download de arquivos do servidor.
            elif serv == '/d':
                tDOWNLOAD = threading.Thread(target=download, args=(conexao, cliente, entrada_comando,))
                tDOWNLOAD.start()
            
            # Download da web.
            elif serv == '/w':
                tWEB = threading.Thread(target=web_download, args=(conexao, cliente, entrada_comando,))
                tWEB.start()
           
        except ConnectionResetError:
            print(f'\nO cliente "{cliente}" deslogou abruptamente!!!\n')
            ATIVIDADE.append(f'{str(datetime.datetime.now())}|Logout abrupto:{sys.exc_info()[0]}|{cliente}')
            ALL_CLIENTS.remove((conexao, cliente))
            break

        except:
            print(f'\nO cliente "{cliente}" forçou a desconexão!!!\n')
            print(f'{sys.exc_info()}')
            ATIVIDADE.append(f'{str(datetime.datetime.now())}|Logout forçado:{sys.exc_info()[0]}|{cliente}')
            ALL_CLIENTS.remove((conexao, cliente))
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
except:
    print(f'ERRO...:{sys.exc_info()[0]}')

