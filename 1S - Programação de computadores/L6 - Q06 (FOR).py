import random
import statistics

quantity = int(input('informe a quantidade de números: '))

list_of_numbers = []
for counter in range(quantity): list_of_numbers.append(random.randint(0, 99))

print(150 * '=')
print(list_of_numbers)
print(f'Média............{statistics.mean(list_of_numbers):.1f}')
print(f'Mediana..........{statistics.median(list_of_numbers)}')
print(f'Variancia........{statistics.pvariance(list_of_numbers):.2f}')
print(f'Desvio padrão....{statistics.pstdev(list_of_numbers):.2f}')
print(150 * '=')