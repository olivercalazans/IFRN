number = int(input('Insira um número: '))
sum = 0
if number > 0:
    for counter in range(number):
        print(number, end='*')
        helper = number * (number - 1)
        sum += helper
        number = number -1
    print(f'\nSoma: {sum}')
elif number == 0: print('O fatorial de 0 é 1.')
else: print('Não existe fatorial de números negativos.')