i = int(input('Informe o primeiro número: '))
j = int(input('Informe o segundo número: '))
n = int(input('Informe quantos múltiplos deseja ver: '))
counter = range = 0
while range < n:
    if counter % i == 0 or counter % j == 0:
        print(counter, end='; ')
        range += 1
    counter += 1
