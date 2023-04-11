import random
quantity = int(input('informe a quantidade de números: '))
numbers = [random.randint(0, 99) for counter in range(quantity)]
print(100 * '=')
print(f'Lista original...... {numbers}.')
numbers.sort(reverse=True)
print(f'Lista decrescente... {numbers}.')
print(100 * '=')