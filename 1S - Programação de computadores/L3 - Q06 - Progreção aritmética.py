inicial = int(input('Informe o valor inicial: '))
razao = int(input('Informe o valor da razão: '))
quantidade = int(input('Informe o a quantidade de números: '))
posicao = int(input('Informe a posição do valor que deseja: '))

quantidade = abs(quantidade)
contador = 1
soma = 0

while contador <= quantidade:
    print(inicial, end=',')
    soma += inicial
    inicial += razao
    contador += 1
    if contador == posicao:
        valor = inicial

if razao > 0:
    print('\nProgreção aritmética crescente.')
elif razao == 0:
    print('\nProgreção aritmética constante.')
else:
    print('\nProgreção aritmética decrescente.')

print(f'A soma dos valores é {soma}')
print('O valor da posição {} é {}.'.format(posicao, valor))
