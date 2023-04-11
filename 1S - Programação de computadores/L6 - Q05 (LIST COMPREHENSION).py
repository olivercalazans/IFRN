import random

quantity = int(input('informe a quantidade de números: '))

list_of_numbers = [random.randint(0, 99) for counter in range(quantity)]
list_of_numbers.sort()
print(150 * '=')
print(list_of_numbers)

average = (sum(list_of_numbers)) / len(list_of_numbers)
print(f'Média............{average:.2f}')

if len(list_of_numbers) % 2 == 0:
    index = len(list_of_numbers) // 2
    median = (list_of_numbers[index] + list_of_numbers[index - 1]) / 2
    print(f'Mediana..........{median}')
elif len(list_of_numbers) % 2 == 1: 
    index = len(list_of_numbers) // 2
    print(f'Mediana..........{list_of_numbers[index]}')

list_variance = [(number - average) ** 2 for number in list_of_numbers]
variance = sum(list_variance) / len(list_of_numbers)
print(f'Variancia........{variance:.2f}')

standard_deviation = variance ** (1/2)
print(f'Desvio padrão....{standard_deviation:.2f}')
print(150 * '=')