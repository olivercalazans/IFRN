a = int(input('Informe o valor de A: '))
b = int(input('Informe o valor de B: '))
c = int(input('Informe o valor de C: '))

delta = b**2 - 4 * a * c

if delta == 0:
    x = ((-b) + delta**(1/2)) / 2 * a
    print(f'O delta de A, B e C é zero, então só existe uma raíz que é {x}.')
elif delta > 0:
    x = ((-b) + delta**(1/2)) / 2 * a
    x2 = ((-b) - delta**(1/2)) / 2 * a
    print(f'As raízes são {x} e {x2}.')
else:
    print('O delta é menor que zero, então não existe solução real.')