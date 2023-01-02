word0 = input('Insira uma palavra: ')
word1 = input('Insira outra palavra: ')
low0, low1 = word0.lower(), word1.lower()
number0, number1 = len(low0), len(low1)

if number0 != number1:
    print('A quantidade de letras das duas palavras são diferentes.')
else:
    helper2, helper3 = low0, low1
    turn = 0
    amount = 0
    while turn < number0:
        helper1 = helper2[turn]
        helper0 = helper3.find(helper1)
        if helper0 >= 0:
            amount += 1
            helper3, helper2 = helper3.replace(helper1, ''),  helper2.replace(helper1, '')
            number0, number1 = len(helper2), len(helper3)
            turn -= 1
        turn += 1

    if helper2 != helper3:
        print(f'As palavras "{word0}" e "{word1}" não são anagramas.')
    else:
        print(f'As palavras "{word0}" e "{word1}" são anagramas.')