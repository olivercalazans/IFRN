valor = int(input('Informe um valor: '))

if valor > 1:
    auxiliar = 1
    while auxiliar <= valor:
        contdiv = 0
        divisor = 1
        while divisor <= valor:
            if auxiliar % divisor == 0:
                contdiv += 1
            if contdiv > 3: break
            divisor += 1 

        if contdiv == 2:
            print(auxiliar, end=',')
        auxiliar += 1
        