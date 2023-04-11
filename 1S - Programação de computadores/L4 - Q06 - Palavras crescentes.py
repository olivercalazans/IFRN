letter = input('Insira uma palavra/frase: ')
number = len(letter)

position = 1
while position <= number:
    print(letter[:position])
    position += 1