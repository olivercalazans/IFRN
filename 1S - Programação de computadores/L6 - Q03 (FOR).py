import random
quantity = int(input('informe a quantidade de números: '))
numbers = []
last = 0
for counter in range(quantity): 
    numbers.append(random.randint(0, 99))
    if numbers[counter] > last: last = numbers[counter]
new_list = []
for counter in range(last + 1):
    for number in numbers:
        if number == counter: new_list.append(number)
print(100 * '=')
print(f'Lista original... {numbers}.')
print(f'Lista crescente.. {new_list}.')
print(100 * '=')