ax = int(input('Informe o valor do x do ponto A: '))
ay = int(input('Informe o valor do y do ponto A: '))
bx = int(input('Informe o valor do x do ponto B: '))
by = int(input('Informe o valor do y do ponto B: '))

h = ((bx - ax)**2 + (by - ay)**2) ** (1/2)

print(f'A distancia entre os pontos A e B é {h:.1f}.')