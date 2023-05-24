import socket

url = input('Informe a url: ')

#  https://www.nasa.gov/sites/default/files/thumbnails/image/nasa-logo-web-rgb.png

NumHost0 = url.find(':')
protoc   = url[:NumHost0]
NumHost1 = url.find('/')
Smaller  = url[NumHost1 + 2:]
NumHost2 = url.find('www.')
host     = url[NumHost2 + 4:]
NumHost3 = host.find('/')
StrImage = host[::-1]
StrNum   = StrImage.find('/')
StrImage = StrImage[:StrNum]

url_host = host[:NumHost3] 
url_img  = host[NumHost3:]
arq_img  = StrImage[::-1]
texto    = arq_img.replace('png', 'txt')


url_request = f'GET {url_img} HTTPS/1.1\r\nHOST: {url_host}\r\n\r\n'

if protoc == 'http':
    host_port = 80
elif protoc == 'https':
    host_port = 443
else:
    host_port = 0

buffer_size = 1024

sock_img = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_img.connect((url_host, host_port))
sock_img.sendall(url_request.encode())

print('\nBaixando a imagem...')
# Montado a variável que armazenará os dados de retorno
data_ret = ''.encode()
while True:
    data = sock_img.recv(buffer_size)
    if not data: break
    data_ret += data

sock_img.close()

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
file_output = open('image.png', 'wb')
file_output.write(image)
file_output.close()