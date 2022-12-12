num = int(input('Insira um valor: '))

soma = 0

soma += num

while num != 0:
    num = int(input('Insira um valor: '))

    if num < 0:
        pass
    else:
        soma += num

print(f'A soma dos números positivos digitados é {soma}.')
