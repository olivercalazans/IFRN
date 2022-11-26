a1 = int(input('Informe o valor do 1° ângulo: '))
a2 = int(input('Informe o valor do 2° ângulo: '))
a3 = int(input('Informe o valor do 3° ângulo: '))

soma = a1 + a2 + a3

if a1 > 0 and a2 > 0 and a3 > 0 and soma == 180:
    if a1 == 90 or a2 == 90 or a3 == 90:
        print('Esse é um triângulo retangulo.')
    elif a1 < 90 and a2 < 90 and a3 < 90:
        print('Esse é um triangulo acutângulo.')
    elif a1 > 90 or a2 > 90 or a3 > 90:
        print('Esse é um triângulo obtusângulo.')
    else:
        ...
else:
    print('Valores inválidos')
    