word = input('Insira uma palavra: ')
counter, vowels, low = 0, 'aeiouáéíóúàèìòùãõâêîôû', word.lower()
for letter in low:
    if letter in vowels:
        counter += 1
print(f'A palavra "{word}" tem {counter} vogais.')