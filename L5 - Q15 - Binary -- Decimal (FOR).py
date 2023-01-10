binary = input('Informe o número binário: ')
binary0, sum = binary[::-1], 0
for counter in range(len(binary0)):
    if binary0[counter] == '1': sum += 2 ** counter
print(f'O valor decimal de {binary} é {sum}')