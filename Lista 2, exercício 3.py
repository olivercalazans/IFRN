a = float(input('Insira o valor de A: '))
b = float(input('Insira o valor de B: '))

if a <= 0 or b <= 0:
    print(f'Informe valores POSITIVOS.')
else:
    ...

h = (a**2 + b**2) ** (1/2)

print('O valor da hipotenusa é {:.1f}.'.format(h))
