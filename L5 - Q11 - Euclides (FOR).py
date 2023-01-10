number1 = int(input('Qual o primeiro número: '))
number2 = int(input('Qual o segundo número: '))
if number1 > number2: bigger,  smaller = number1, number2
else: bigger, smaller = number2, number1
for counter in range(100):
    helper = bigger % smaller
    if helper == 0: break
    bigger = smaller
    smaller = helper
print(f'O MDC de {number1} e {number2} é {smaller}.')