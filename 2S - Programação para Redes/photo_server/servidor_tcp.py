import socket, sys, os

# Criando conexão e aguandando cliente.
try: 
    # Criando socket TCP.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Vinculando o socket a tupla.
    sock.bind(('localhost', 50000))

    # Limitando o número de conexoes.
    sock.listen(1)
except:
    print(f'ERRO...:{sys.exc_info()}')
    sys.exit()
else:
    print(f'\nSERVIDOR ATIVO: {sock.getsockname()}')
    print('Aguardando coenxão...')

try:
    while True:
        # Aceitando conexão.
        conexao, cliente = sock.accept()
        print(f'\nConectado por: {cliente}')
        print('Aguardando pedido...')
        
        while True:
            # Recebendo o nome e verificando se existe.
            pedido = (conexao.recv(10240)).decode('utf-8')
            if pedido.upper() == 'EXIT':
                print(f'\nO cliente "{cliente}" desconectou.')
                break
            DIRETORIO  = os.path.dirname(os.path.abspath(__file__))
            DIRETORIO += '\\img_server\\'
            nome_arq  = DIRETORIO + pedido
            imagens = os.listdir(DIRETORIO)
            if not pedido in imagens:
                conexao.send('false'.encode('utf-8'))
                sock.close()
                sys.exit()
            else: 
                conexao.send('true'.encode('utf-8'))

            if pedido.upper() == 'EXIT': break

            print(f'\nEnviando header do {pedido}')

            # Enviando o header com o tamanho do arquivo.
            tamanho_arquivo = os.path.getsize(nome_arq)
            pacotes_int = tamanho_arquivo // 10240
            pacotes_flo = tamanho_arquivo / 10240
            if pacotes_flo > pacotes_int:
                pacotes_int += 1
            header = f'SIZE:{tamanho_arquivo},PACOTES:{pacotes_int}'
            conexao.send(header.encode('utf-8'))

            # Enviando arquivo.
            pacotes_enviados = 0
            with open(nome_arq, 'rb') as arquivo:
                while True:
                    dados_retorno = arquivo.read(10240)
                    if not dados_retorno: break
                    conexao.send(dados_retorno)
                    pacotes_enviados += 1
                    sys.stdout.write(f'\rPacotes enviados: {pacotes_enviados}')
                    sys.stdout.flush()
                print(f'\nArquivo "{pedido}" enviado.')
except KeyboardInterrupt:
    print('CTRL + C foi pressionado.')
    sock.close()
    sys.exit()
except SystemExit:
    print('\nArquivo não encontrado.') 
except:
    print(f'ERRO...:{sys.exc_info()}')
    sock.close
finally:
    sock.close()
