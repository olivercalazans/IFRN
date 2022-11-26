ano = int(input('Insira um ano entre 1900 e 2100: '))

if ano > 2100 or ano < 1900:
    print('Ano invalido. Tente novamente.')
elif ano % 4 == 0:
    print(f'{ano} é bissexto')
else:
    print(f'{ano} não é bissexto.')