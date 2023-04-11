numero = int(input('informe um valor inteiro: '))

while numero != 0:
    if numero % 2 == 0:
        print(f'{numero} é um número par')
    else:
        print(f'{numero} é um número impar.')

    numero = int(input('informe um valor inteiro: '))
else:
    print('FIM')