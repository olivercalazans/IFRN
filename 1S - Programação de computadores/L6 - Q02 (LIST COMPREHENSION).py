import random

n = int(input('Informe a quantidade de números: '))
numbers = [random.randint(0, 99) for counter in range(n)]
second_list = [0, 0, 0, 0]
for counter in numbers:
    if counter > 74: second_list[3] += 1
    elif counter > 49: second_list[2] += 1
    elif counter > 24: second_list[1] += 1
    elif counter > 0: second_list[0] += 1
print(150 * '=')
print(numbers)
print(f'Quantidade de números por quartil:\n1° quartil....{second_list[0]}\n2° quartil....{second_list[1]}\n3° quartil....{second_list[2]}\n4° quartil....{second_list[3]}')
print(150 * '=')