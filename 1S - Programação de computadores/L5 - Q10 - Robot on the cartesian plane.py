x = int(input('Informe o valor de X da posição inicial: '))
y = int(input('Informe o valor de Y da posição inicial: '))
a, b = x, y
letters = input('Insira as letras para movimentar o robô: ')
low, ways = letters.lower(), 'udrlonew'
length0 = len(low)
length2 = length0
numbers, moviments = '', 0
for letter in ways:
    if letter in low:
        low = low.replace(letter, '')
        length0 = len(low)
        helper1 = (length0 - length2) * (-1)
        moviments += helper1
        helper1 = str(helper1)
        numbers += helper1
        length2 = length0
    else: numbers += '0'
up, down, right, left, ul, ur, dr, dl = 0, 0, 0, 0, 0, 0, 0, 0
for counter1 in range(len(numbers)):
    helper = int(numbers[counter1])
    if counter1 == 0:
        y += helper
        up += helper
    elif counter1 == 1:
        y -= helper
        down += helper
    elif counter1 == 2:
        x += helper
        right += helper
    elif counter1 == 3:
        x -= helper
        left += helper
    elif counter1 == 4:
        y += helper
        x -= helper
        ul += helper
    elif counter1 == 5:
        y += helper
        x += helper
        ur += helper
    elif counter1 == 6:
        y -= helper
        x += helper
        dr += helper
    elif counter1 == 7:
        y -= helper
        x -= helper
        dl += helper
if a == 0 and b == 0: print(f'O robô iniciou nos pontos ({a}, {b}) que é no centro do plano cartesiano.')
elif a == 0 and (b > 0 or b < 0): print(f'O robô iniciou nos pontos ({a}, {b}) que é em cima do eixo X.')
elif b == 0 and (a > 0 or a < 0): print(f'O robô iniciou nos pontos ({a}, {b}) que é em cima do eixo Y.')
elif a > 0 and b > 0: print(f'O robô iniciou nos pontos ({a}, {b}) que é no 1° quadrante.')
elif a < 0 and b > 0: print(f'O robô iniciou nos pontos ({a}, {b}) que é no 2° quadrante.')
elif a < 0 and b < 0: print(f'O robô iniciou nos pontos ({a}, {b}) que é no 3° quadrante.')
elif a > 0 and b < 0: print(f'O robô iniciou nos pontos ({a}, {b}) que é no 4° quadrante.')
if x == 0 and y == 0: print(f'O robô terminou nos pontos ({x}, {y}) que é no centro do plano cartesiano.')
elif x == 0 and (y > 0 or y < 0): print(f'O robô terminou nos pontos ({x}, {y}) que é em cima do eixo X.')
elif y == 0 and (x > 0 or x < 0): print(f'O robô terminou nos pontos ({x}, {y}) que é em cima do eixo Y.')
elif x > 0 and y > 0: print(f'O robô terminou nos pontos ({x}, {y}) que é no 1° quadrante.')
elif x < 0 and y > 0: print(f'O robô terminou nos pontos ({x}, {y}) que é no 2° quadrante.')
elif x < 0 and y < 0: print(f'O robô terminou nos pontos ({x}, {y}) que é no 3° quadrante.')
elif x > 0 and y < 0: print(f'O robô terminou nos pontos ({x}, {y}) que é no 4° quadrante.')
print(f'O robô fez {moviments} movimentos.\nOs movimentos foram: cima: {up}, baixo: {down}, direita: {right}, esquerda: {left},\ncima-esquerda: {ul}, cima-direita: {ur}, baixo-direita: {dr}, baixo-esquerda: {dl}.')