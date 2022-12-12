num = int(input('Informe um número: '))

aux = 0
contador = 1
cont2 = 0

while aux <= num:
    aux += contador
    contador += 1
    
    if aux == num:
        print(f'{num} é triangular.')
        cont2 += 1
        
if cont2 == 0:
    print(f'{num} não é triangular.')
