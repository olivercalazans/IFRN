import socket, threading, sys, requests, os
#from servicos import *


# ================================= ÁREA DE CONSTANTES ================================================

ALL_CLIENTS  = list()  # Pessoas logadas ao servidor.
LISTA_IPS    = list()
CODIGO_TRAD  = 'utf-8'
DIRETORIO    = os.path.dirname(os.path.abspath(__file__))
SERVER_FILES = DIRETORIO + '\\server_files\\'

# ================================== ÁREA DE FUNÇÕES ==================================================

def telegram(logg):
    API_KEY = '5963236170:AAHAGkg0acf4Wp3-kZac-zlYKD6DpouHYoI'
    url_req = f'https://api.telegram.org/bot{API_KEY}'
    requisicao = requests.get(url_req + '/getUpdates')
    retorno = requisicao.json()
    id_chat = retorno['result'][0]['message']['chat']['id']
    mensagem = logg
    resposta = {'chat_id':id_chat,'text':mensagem}
    envio = requests.post(url_req + '/sendMessage', data=resposta)

def lista_ips(conexao, cliente):
    ips = ''
    for ip in LISTA_IPS:
        if ip != cliente:
            ips += f'{ip}/'
    conexao.send(ips.encode(CODIGO_TRAD))

# Essa função faz uma lista dos arquivos do servidor.
def lista_arquivos():
    nomes     = os.listdir(SERVER_FILES)
    full_list = [f'{nome}: {os.path.getsize(SERVER_FILES + nome)} bytes' for nome in nomes]
    return full_list

# Thread onde o cliente faz a interação com o servidor ------------------------------------
def servicos(conexao, cliente):
    logg = f'Login: {cliente}'
    aviso_in = threading.Thread(target=telegram, args=(logg,))
    aviso_in.start()
    print(logg)
    
    while True:
        entrada_comando = (conexao.recv(1024)).decode(CODIGO_TRAD)
        serv = entrada_comando[:2]
        
        # Comando para deslogar do servidor
        if serv == '/q':
            logg = f'Logout: {cliente}'
            aviso_out = threading.Thread(target=telegram, args=(logg,))
            aviso_out.start()
            print(logg)
            ALL_CLIENTS.remove((conexao, cliente))
        if serv == '/l':
            all_ips = threading.Thread(target=lista_ips, args=(conexao, cliente,))
            all_ips.start()


# =====================================================================================================

# Ativando servidor e esperando conexões.
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', 50000))
    sock.listen(5)
except:
    print(f'ERRO...:{sys.exc_info()}')
    sys.exit()
else:
    print(f'\nSERVIDOR ATIVO: {sock.getsockname()}\n')

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

