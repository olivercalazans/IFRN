number = int(input('Insira um número: '))
binary, number0 = '', number
for counter in range(50):
    rest = number % 2
    binary += str(rest)
    number //= 2
    if number < 1: break
print(f'O binário de {number0} é {binary[::-1]}')