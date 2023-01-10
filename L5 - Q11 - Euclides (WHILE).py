number1 = int(input('Insira o primero número: '))
number2 = int(input('Insira o segundo número: '))
if number1 > number2: bigger,  smaller = number1, number2
else: bigger, smaller = number2, number1
while bigger % smaller > 0:
    helper = bigger % smaller
    bigger = smaller
    smaller = helper
print(f'O MDC de {number1} e {number2} é {smaller}.')