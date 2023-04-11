a = int(input('Informe o tamanho do 1° lado: '))
b = int(input('Informe o tamanho do 2° lado: '))
c = int(input('Informe o tamanho do 3° lado: '))

m1 = b - c
m2 = a - c
m3 = a - b 

if m1 < 0:
    m1 = m1 * (-1)
elif m2 < 0:
    m2 = m2 * (-1)
elif m3 < 0:
    m3 = m3 * (-1)
else:
    ...

l1 = m1 < a and a < b + c
l2 = m2 < b and b < a + c
l3 = m3 < c and c < a + b 

if l1 == True and l2 == True and l3 == True:
    if a == b and b == c:
        print('Esse triangulo é equilátero.')
    elif a == b or a == c or b == c:
        print('Esse triangulo é isósceles.')
    else:
        print('Esse triangulo é escaleno.')
else:
    print('Valor inválido.')


