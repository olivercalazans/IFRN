number1 = int(input('Insira o primero número: '))
number2 = int(input('Insira o segundo número: '))
bigger, smaller = number1, number2
numbers, counter = '', 2
for counter0 in range(100):
    if bigger == 1 or smaller == 1: break
    if bigger % counter == 0 and smaller % counter == 0:
        numbers += str(counter)
        bigger //= counter
        smaller //= counter
    else:
        if bigger % counter == 0 or smaller % counter == 0:
            if bigger % counter == 0: bigger //= counter
            elif smaller % counter == 0: smaller //= counter
        else: counter += 1
multiplication = 1
for number in numbers: multiplication *= int(number)
print(f'O maior divisor comum de {number1} e {number2} é {multiplication}.')