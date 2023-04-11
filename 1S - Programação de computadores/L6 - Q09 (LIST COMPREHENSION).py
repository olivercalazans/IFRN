import random

quantity = int(input('informe a quantidade de números: '))
numbers = [random.randint(0, 1000) for counter in range(quantity)]

number = int(input('Digite um número entre 0 e 1000: '))
while number < 0:
    number = int(input('Digite um número ENTRE 0 e 1000: '))

print(150 * '=')
print(numbers)
if number in numbers: 
    print(f'O número {number} está na lista.')
    print(f'Ele está na posição {numbers.index(number)}.')
else: print(f'O número {number} não está na lista.')
print(150 * '=')