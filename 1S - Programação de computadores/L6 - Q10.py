length = int(input('Informe a quantidade de elementos da lista: '))

list_of_numbers = []
number = int(input('Informe um número para a lista: '))
list_of_numbers.append(number)
print(list_of_numbers)

while number != 0:
    number = int(input('Informe outro número para a lista: '))
    list_of_numbers.append(number)
    list_of_numbers.sort()
    if len(list_of_numbers) > length:
        list_of_numbers.remove(list_of_numbers[length])
    print(list_of_numbers)

print('FIM')