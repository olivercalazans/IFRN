import random
quantity = int(input('informe a quantidade de números: '))
numbers = [random.randint(0, 99) for counter in range(quantity)]
last = 0
for counter in range(len(numbers)): 
    if numbers[counter] > last: last = numbers[counter]
new_list = [number for counter in range(last + 1) for number in numbers if number == counter]
print(100 * '=')
print(f'Lista original... {numbers}.')
print(f'Lista crescente.. {new_list}.')
print(100 * '=')