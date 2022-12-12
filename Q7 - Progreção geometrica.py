inicial = int(input('Informe o valor inicial: '))
razao = int(input('Informe o valor da razão: '))
quantidade = int(input('Informe o a quantidade de números: '))
posicao = int(input('Informe a posição do valor que deseja: '))

if inicial == 0 or razao == 0 or quantidade == 0 or posicao == 0:
    print('Digite números DIFERENTES de zero.')
else:
    quantidade = abs(quantidade)
    contador = 1
    soma = 0

    while contador <= quantidade:
        print(inicial, end=',')
        soma += inicial
        inicial *= razao
        contador += 1
        if contador == posicao:
            valor = inicial

    if razao == 1:
        print('\nProgreção geometrica constante.')
    elif inicial > 0 and razao > 0:
        print('\nProgreção geomerica crescente.')
    elif inicial < 0 and razao > 0:
        print('\nProgreção geometrica decrecentes.')
    else:
        print('\nProgreção geometrica oscilante.')

    print(f'A soma dos valores é {soma}')
    print('O valor da posição {} é {}.'.format(posicao, valor))
