contador = 1000
limite = 2000

while contador <= limite:
    if contador % 11 == 5:
        print(contador, end=',')
    contador += 1