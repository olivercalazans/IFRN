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
name_img  = reversed_url[::-1]
name_img  = name_img.split('.')
name_img  = name_img[0]

# Dados que serão usados. Há mais dados depois desses.
protocol  = url[:seacher0]
url_host  = url0[:seacher2]
url_image = url0[seacher2:]
arq_image = name_img

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
        print('\nApenas as URLs com protocolos HTTP e HTTPS são aceitas.')
        print(f'Protocolo da URL informada: {protocol}')
        print('Os demais protocolos serão adicionados em breve.')
        sys.exit()
except:
    print('\nErro ao criar a conexão')
    print(print(f'ERRO...:{sys.exc_info()[0]}'))
    sys.exit()

print('\nBaixando a imagem...')
# Montado a variável que armazenará os dados de retorno
data_ret = ''.encode()
while True:
    data = sock_img.recv(buffer_size)
    if not data: break
    data_ret += data
    sys.stdout.write(f'\rBytes baixados: {len(data_ret)} bytes')
    sys.stdout.flush()

# Obtendo o tamanho da imagem e o tipo de aquivo.
type_name = ''
confir1   =  confir2  =  False
img_size  = -1
tmp = data_ret.split('\r\n'.encode())
for line in tmp:
    # Tamamho do cabeçalho.
    if 'Content-Length:'.encode() in line:
        img_size = int(line.split()[1])
        confir1 = True
    # Tipo de arquivo.
    if 'Content-Type:'.encode() in line:
        type_name = str(line.split()[1])
        confir2 = True
    if confir1 == True and confir2 == True: break

# Dados que serão usados.
type_name  = type_name.split('/')[1]
type_name  = type_name.replace("'","")
txt_image  = name_img + '.txt'
arq_image += f'.{type_name}'
header_len = len(data_ret) - img_size

print('\n')
print('-' * 100)
print(f'Protocolo..............: {protocol}')
print(f'URL do host............: {url_host}')
print(f'URL da imagem..........: {url_image}')
print(f'Arquivo da imagem......: {arq_image}')
print(f'Texto da imagem........: {txt_image}')
print(f'Tamanho do cabeçalho...: {header_len} bytes')
print(f'Tamanho da Imagem......: {img_size} bytes')
print(f'Tamanho total..........: {len(data_ret)} bytes')
print('-' * 100)

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
    print('\nErro ao salvar o arquivo.')
    print(print(f'ERRO...:{sys.exc_info()[0]}'))
    sys.exit()
