number1 = int(input('Insira o primero número: '))
number2 = int(input('Insira o segundo número: '))
bigger, smaller = number1, number2
numbers, counter = '', 2
while bigger > 1 and smaller > 1:
    if bigger % counter == 0 and smaller % counter == 0:
        numbers += str(counter)
        bigger //= counter
        smaller //= counter
    else:
        if bigger % counter == 0 or smaller % counter == 0:
            if bigger % counter == 0: bigger //= counter
            elif smaller % counter == 0: smaller //= counter
        else: counter += 1
counter0, multiplication = 0, 1
while counter0 < len(numbers) :
    multiplication *= int(numbers[counter0])
    counter0 += 1
print(f'O maior divisor comum de {number1} e {number2} é {multiplication}.')