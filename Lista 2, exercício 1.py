a = int(input('Insira um valor: '))
b = int(input('Insira outro valor: '))

print('Antes: x era {} e y era {}.'.format(a, b))

c = a
a = b
b = c

print('Agora: x é {} e y é {}.'.format(a, b))
