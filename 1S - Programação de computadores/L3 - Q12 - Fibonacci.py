num = int(input('Informe a quantidade de números: '))

aux0 = 0
contador = 1
aux1 = 0
aux2 = 0
while aux0 < num:
    print(contador,end=',')
    aux2 = contador
    contador += aux1
    aux1 = aux2    
    aux0 += 1