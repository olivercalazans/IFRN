word = input('Insira uma palavra: ')
for counter in range(len(word)):
    print(word[:counter + 1])