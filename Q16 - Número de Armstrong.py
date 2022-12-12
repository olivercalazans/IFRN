num = int(input('Insira um número: '))

num_aux = num
aux1 = 1
contador = 0

while aux1 <= num:
    aux1 *= 10
    contador +=1

aux2 = aux1 / 10
digito = 0
somat = 0
aux3 = 0
nume_aux2 = 0

while aux2 >= 1:
    nume_aux2 = num_aux // aux2
    digito = nume_aux2
    soma = digito ** contador
    somat += soma
    num_aux %= aux2
    aux2 /= 10

tf = num == somat

if tf == True:
    print(f'{num} é um número de Armstrong.')
else:
    print(f'{num} não é um número de Armstrong.')
