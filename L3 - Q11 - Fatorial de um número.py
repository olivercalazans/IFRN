num = int(input('Insira um valor: '))

if num == 0:
    print('O fatorial de zero é 1.')
elif num < 0:
    print('Não existe fatorial de número negativo.')
else:
    num1 = num
    aux = num - 1
    while aux > 0:
        num1 *= aux
        aux -= 1
    
    print(f'O fatorial de{num} é {num1}.')
