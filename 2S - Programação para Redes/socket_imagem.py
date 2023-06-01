import socket, sys, ssl

# URL PARA TESTES: https://www.nasa.gov/sites/default/files/thumbnails/image/nasa-logo-web-rgb.png

url = input('Informe a URL: ')

# Manipulando a url/string para poder pegar os dados necessários.
seacher0     = url.find(':')
seacher1     = url.find('//')
url0         = url[seacher1 + 2:]
seacher2     = url0.find('/')
reversed_url = url[::-1]
seacher3     = reversed_url.find('/')
reversed_url = reversed_url[:seacher3]
finder_type  = reversed_url[::-1]
finder_type  = finder_type.split('.')
replace_txt  = finder_type[-1]

# Dados que serão usados.
protocol  = url[:seacher0]
url_host  = url0[:seacher2]
url_image = url0[seacher2:]
arq_image = reversed_url[::-1]
txt_image = arq_image.replace(replace_txt,'txt')

print(f'Protocolo...........: {protocol}')
print(f'URL do host.........: {url_host}')
print(f'URL da imagem.......: {url_image}')
print(f'Arquivo da imagem...: {arq_image}')
print(f'Texto da imagem.....: {txt_image}')

# Criando conexão
try: 
    url_request = f'GET {url_image} HTTP/1.1\r\nHOST: {url_host}\r\nConnection:close\r\n\r\n'
    sock_img = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    buffer_size = 1024

    # Verificando o protocolo.
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
    else:
        print('Apenas as URLs com protocolos HTTP e HTTPS são aceitas.')
        print(f'Protocolo da URL informada: {protocol}')
        print('Os demais protocolos serão adicionados em breve.')
        sys.exit()
except:
    print('Erro ao criar a conexão')
    print(print(f'ERRO...:{sys.exc_info()[0]}'))
    sys.exit()

print('\nBaixando a imagem...')
# Montado a variável que armazenará os dados de retorno
data_ret = ''.encode()
while True:
    data = sock_img.recv(buffer_size)
    if not data: break
    data_ret += data

# Obtendo o tamanho da imagem
img_size = -1
tmp = data_ret.split('\r\n'.encode())
for line in tmp:
   if 'Content-Length:'.encode() in line:
      img_size = int(line.split()[1])
      break
print(f'\nTamanho da Imagem: {img_size} bytes')

# Separando o Cabeçalho dos Dados
delimiter = '\r\n\r\n'.encode()
position  = data_ret.find(delimiter)
headers   = data_ret[:position]
image     = data_ret[position+4:]

# Salvando a imagem
file_output = open(f'{arq_image}', 'wb')
file_output.write(image)
file_output.close()

# Escrevendo arquivo com os dados do header.
try:
    with open(f'{txt_image}','w',encoding='utf-8') as writing_header:
        writing_header.write(headers.decode('utf-8'))
except:
    print('Erro ao salvar o arquivo.')
    print(print(f'ERRO...:{sys.exc_info()[0]}'))
    sys.exit()
