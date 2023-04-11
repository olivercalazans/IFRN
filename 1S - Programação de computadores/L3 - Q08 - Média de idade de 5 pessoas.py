idade = int(input('informe sua idade: '))
sexo = input('Informe seu sexo, H para homem e M para mulher: ')
sexo = sexo.upper()

contador = 1
soma = 0
soma += idade
somah = 0
contadorh = 0
contadorm = 0
somam = 0

if sexo == 'H':
    contadorh += 1
    somah += idade
elif sexo == 'M':
    contadorm += 1
    somam += idade

while contador < 5:
    idade = int(input('informe sua idade: '))
    sexo = input('Informe seu sexo, H para homem e M para mulher: ')
    sexo = sexo.upper()
    soma += idade

    if sexo == 'H':
        contadorh += 1
        somah += idade
    elif sexo == 'M':
        contadorm += 1
        somam += idade
    contador += 1

if contadorh == 0:
    media = soma / contador
    mediam = somam / contadorm
    print(f'A média das mulheres é {mediam:.1f}.')
elif contadorm == 0:
    media = soma / contador
    mediah = somah / contadorh
    print(f'A média dos homens é {mediah:.1f}.')
else:      
    media = soma / contador
    mediah = somah / contadorh
    mediam = somam / contadorm
    print(f'A idade média das 5 pessoas é {media:.1f}.A média dos homens é {mediah:.1f}. A média das mulheres é {mediam:.1f}.')
    