word = input('Insira uma palavra: ')
low, helper = word.lower(), 0
reverse = low[::-1]
for counter in range(len(reverse)):
    if reverse[counter] == low[counter]:
        helper += 1
if len(low) == helper: print(f'A palavra "{word}" é um palindromo.')
else: print(f'A palavra "{word}" não é um palindromo.')