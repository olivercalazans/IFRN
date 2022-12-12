numero = int(input('Insira um número: '))
binario = ''
while numero > 0:
    resto = numero % 2
    numero = numero // 2
    binario = str(resto) + binario
    print(resto, end='')
    