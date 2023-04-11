import random

PALAVRAS_CHAVE = ['gato', 'abacaxi', 'roma', 'celular', 'livro', 'caneta', 'garrafa', 'camisa', 'espada', 'botas']
P1 = PALAVRA_CHAVE = PALAVRAS_CHAVE[random.randint(0, 9)]
letter = input('Insira uma letra: ')
low = letter.lower()
wrong_letters = []
right_letters = []
number = len(PALAVRA_CHAVE)
wrongs = 0
while wrongs <= 5 and number > 1:
    if letter in wrong_letters or letter in right_letters:
        print(150 * '=')
        letter = input('Essa letra já foi escolhida. Escolha outra letra: ')
        print(f'Letras certas: {right_letters}\n Letras erradas: {wrong_letters}')
        low = letter.lower()
    else:
        helper0 = PALAVRA_CHAVE.find(low)
        if helper0 < 0:
            wrongs += 1
            if wrongs < 6:
                wrong_letters.append(low)
                print(150 * '=')
                letter = input(f'LETRA ERRADA. Você errou {wrongs}/6.\nFaltam {number} letras.\nLetras certas: {right_letters}\nLetras já usadas: {wrong_letters}\nEscolha outra letra: ')
                low = letter.lower()
            else: break
        else:
            PALAVRA_CHAVE = PALAVRA_CHAVE.replace(low, '')
            number = len(PALAVRA_CHAVE)
            right_letters.append(low)
            print(150 * '=')
            letter = input(f'ENCONTROU UMA LETRA!.\nVocê errou {wrongs}/6.\nFaltam {number} letras.\nLetras certas: {right_letters}\nLetras já usadas: {wrong_letters}.\nEscolha outra letra: ')
            low = letter.lower()
if wrongs == 6:
    print(150 * '=')
    print(f'GAME OVER\nVocê perdeu todas as chances. A palavra era ({P1})')
    print(150 * '=')
else:
    print(150 * '=')
    print(f'PARABÉNS!! Você descobriu a palavra escondida ({P1}).')
    print(150 * '=')