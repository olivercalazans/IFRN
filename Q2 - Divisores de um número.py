numero = int(input('Insira um número inteiro: '))

numero = abs(numero)

if numero != 0:
    contador = 0
    divisor = 1

    while divisor <= numero:
        if numero % divisor == 0:
            print(divisor, end=',')
            contador += 1
        divisor += 1

    if contador == 2:
        print(f'{numero} é um número primo.')
else:
    print('Zero não tem divisores.')
    
