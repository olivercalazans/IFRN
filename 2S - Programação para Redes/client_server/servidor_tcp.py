import socket, sys, os

# Criando socket TCP.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vinculando o socket a tupla.
sock.bind(('localhost', 50000))

# Limitando o número de conexoes.
sock.listen(1)
print(f'\nSERVIDOR ATIVO: {sock.getsockname()}')
print('Aguardando coenxão...')

try:
    while True:
        # Aceitando conexão.
        conexao, cliente = sock.accept()
        print(f'\nConectado por: {cliente}')
        print('Aguardando pedido...')
        while True:
            pedido = (conexao.recv(10240)).decode('utf-8')
            if pedido.upper() == 'EXIT':
                print(f'\nO cliente "{cliente}" desconectou.')
            else:
                DIRETORIO = os.path.dirname(os.path.abspath(__file__))
                nome_arq  = DIRETORIO + '\\img_server\\' + pedido
                print(f'\nEnviando: {pedido}')

                # Enviando o header com o tamanho do arquivo.
                tamanho_arquivo = os.path.getsize(nome_arq)
                header = f'Size:{tamanho_arquivo}'
                sock.send(header.encode('utf-8'))

                # Enviando arquivo.
                with open(nome_arq, 'rb') as arquivo:
                    while True:
                        dados_retorno = arquivo.read(10240)
                        if not dados_retorno: break
                        conexao.send(dados_retorno)
                print(f'Arquivo: {pedido} enviado.')
except KeyboardInterrupt:
    print('CTRL + C foi pressionado.')
    sock.close()
except:
    print(f'ERRO...:{sys.exc_info()}')
    sock.close
finally:
    sock.close()