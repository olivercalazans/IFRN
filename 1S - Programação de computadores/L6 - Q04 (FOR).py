import random
quantity = int(input('informe a quantidade de números: '))
numbers = []
for counter in range(quantity): numbers.append(random.randint(0, 99))
print(100 * '=')
print(f'Lista original...... {numbers}.')
numbers.sort(reverse=True)
print(f'Lista decrescente... {numbers}.')
print(100 * '=')