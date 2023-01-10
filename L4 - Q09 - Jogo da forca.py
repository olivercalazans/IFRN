PALAVRA_CHAVE = 'abacaxi'
letter = input('Insira uma letra: ')
low = letter.lower()
used = ''
number = len(PALAVRA_CHAVE)
wrongs = 0
while wrongs <= 5 and number > 1:
    if letter in used:
        letter = input('Essa letra já foi escolhida. Escolha outra letra: ')
        low = letter.lower()
    else:
        helper0 = PALAVRA_CHAVE.find(low)
        if helper0 < 0:
            wrongs += 1
            if wrongs < 6:
                used += ' ' + low
                letter = input(f'LETRA ERRADA. Você errou {wrongs}/6.\nFaltam {number} letras.\nLetras já usadas: {used}\nEscolha outra letra: ')
                low = letter.lower()
            else: break
        else:
            PALAVRA_CHAVE = PALAVRA_CHAVE.replace(low, '')
            number = len(PALAVRA_CHAVE)
            used += ' ' + low
            letter = input(f'ENCONTROU UMA LETRA!.\nVocê errou {wrongs}/6.\nFaltam {number} letras.\nLetras já usadas: {used}.\nEscolha outra letra: ')
            low = letter.lower()
if wrongs == 6:
    print('GAME OVER\nVocê perdeu todas as chances.')
else:
    print('PARABÉNS!! Você descobriu a palavra escondida.')
