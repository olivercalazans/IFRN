valor = int(input('Insira um valor diferente de zero (0 = ENCERRAR): '))

soma = 0
menor = valor
maior = valor
contador = 0

while valor != 0:
    soma += valor
    contador += 1
    if maior < valor:
        maior = valor
    elif menor > valor:
        menor = valor
    valor = int(input('Insira um valor diferente de zero (0 = ENCERRAR): '))

media = soma / contador

print(f'A média dos valores é {media}. O maior número foi {maior} e o menor foi {menor}.')
