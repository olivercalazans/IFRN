import random
import numpy as np

quantity = int(input('informe a quantidade de números: '))

list_of_lists = []
for counter in range(quantity):
    sublist0 = []
    for number in range(quantity):
        sublist0.append(random.randint(0, 9))
    list_of_lists.append(sublist0)

array = np.array(list_of_lists)
det = np.linalg.det(array)

print(150 * '=')
print(array)
print(f'Determinante: {det:.2f}')
print(150 * '=')