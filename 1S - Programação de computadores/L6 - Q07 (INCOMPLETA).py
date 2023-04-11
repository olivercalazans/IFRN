import random
import numpy as np

quantity = int(input('informe a quantidade de números: '))

list_of_lists = []


for counter in range(quantity):
    sublist = []
    for counter0 in range(quantity):
        sublist.append(random.randint(0, 9))
    list_of_lists.append(sublist)

x = []
print(list_of_lists)

for counter in range(quantity):
    sublist = list_of_lists[counter]
    number = sublist[counter]
    x.append(number)

print(x)


