import socket, os, sys

# Criando um objeto socket.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ligando socket a porta.
sock.connect(('localhost',50000))

while True:
    # Solicitando o arquivo.
    nome_arq = input('\nNome do arquivo: ')
    
    if nome_arq.lower() == 'exit': 
        sock.send(nome_arq.encode('utf-8'))
        break

    # Enviando o nome do arquivo.
    print(f'Arquivo solicitando: {nome_arq}')
    sock.send(nome_arq.encode('utf-8'))

    # Recebendo informações.
    confirmacao = (sock.recv(10240)).decode('utf-8')
    
    if confirmacao == 'false':
        print(f'O arquivo "{nome_arq}" não existe.')
    else:
        dados = (sock.recv(10240)).decode('utf-8')

        tamanho_total = quantidade_pacotes = '?????'
        if 'SIZE:' in dados.upper() and 'PACOTES' in dados.upper():
            aux = dados.split(',')
            tamanho_total = int(aux[0].split(':')[-1])
            quantidade_pacotes = int(aux[-1].split(':')[-1])

        # Criando diretório para salvar o arquivo.
        DIRETORIO  = os.path.dirname(os.path.abspath(__file__))
        DIRETORIO += '\\img_client\\'
        
        try:
            os.mkdir(DIRETORIO)
        except FileExistsError:
            print('O diretório já existe.')
        except:
            print(f'ERRO...:{sys.exc_info()[0]}')
        else:
            print('Diretório criado com sucesso.')

        # Gravando os dados em um arquivo.
        print(f'Gravando o arquivo: {nome_arq} ({tamanho_total} bytes)')
        caminho = DIRETORIO + nome_arq
        bytes_recebidos = pacotes = 0
        
        # Recebendo o conteúdo.
        with open(caminho, 'wb') as arquivo:
            while True:
                dados_recebidos = sock.recv(10240)
                if not dados_recebidos: break
                print(f'Pacote ({pacotes}) - Dados recebidos: {dados_recebidos} bytes')
                arquivo.write(dados_recebidos)
                bytes_recebidos += len(dados_recebidos)
                if bytes_recebidos >= tamanho_total: break
                pacotes += 1
                sys.stdout.write(f'\rPacotes recebidos: {pacotes}/{quantidade_pacotes}')
                sys.stdout.flush()
                sys.stdout.write(f'\rDados processados: {bytes_recebidos}/{tamanho_total}')
                sys.stdout.flush()

    # Fechando socket.
    sock.close()
