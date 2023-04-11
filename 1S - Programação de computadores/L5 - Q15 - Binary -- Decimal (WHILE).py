binary = input('Informe o número binário: ')
binary0, sum , counter = binary[::-1], 0, 0
while counter < len(binary0):
    if binary0[counter] == '1': 
        sum += 2 ** counter
    counter += 1
print(f'O valor decimal de {binary} é {sum}')