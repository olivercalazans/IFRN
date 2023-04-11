num1 = int(input('Insira um número inteiro: '))

if num1 == 0:
    print(f'{num1} é nulo.')
elif num1 > 0 and num1 % 2 == 0:
    print(f'{num1} é positivo e par.')
elif num1 > 0 and num1 % 2 == 1:
    print(f'{num1} é positivo e impar.')
elif num1 < 0 and num1 % -2 == 0:
    print(f'{num1} é negativo e par.')
else:
    print(f'{num1} é negativo e impar.')
