word = input('Insira uma palavra/frase: ')
low = word.lower()
number = len(low)

letter = 'aáàâãeéèêiíìîoóòôõuúùû'
letter_number = len(letter)

turn = 0
counter = 0

while turn < number:
    letter_position = 0

    while letter_position < letter_number:

        l1 = low[turn]
        l2 = letter[letter_position]
        p = l1 == l2
        
        if p == True:
            counter += 1
        
        letter_position += 1
    
    turn += 1

print(f'A palavra/frase "{word}" tem {counter} vogais.')