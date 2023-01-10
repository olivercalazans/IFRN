x = int(input('Informe o valor de X: '))
y = int(input('Informe o valor de Y: '))

if x > 0 and y > 0:
    print('O ponto está no 1° quadrante.')
elif x < 0 and y > 0:
    print('O ponto está no 2° quadrante.')
elif x < 0 and y < 0:
    print('O ponto está no 3° quadrante.')
else:
    print('O ponto está no 4° quadrante.')
