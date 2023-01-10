peso = float(input('Informe o seu peso em quilogramas (Kg): '))
altura = float(input('Informe a sua altura em metros: '))

imc = peso / altura ** 2 

if imc >= 40:
    print(f'Seu IMC é {imc:.1f}. Classificação: OBESIDADE GRAU III OU MÓRBIDA.')
elif imc >= 35:
    print(f'Seu IMC é {imc:.1f}. Classificação: OBESIDADE GRAU II.')
elif imc >= 30:
    print(f'Seu IMC é {imc:.1f}. Classificação: OBESIDADE GRAU I.')
elif imc >= 25:
    print(f'Seu IMC é {imc:.1f}. Classificação: OBESIDADE GRAU III OU MÓRBIDA.')
elif imc >= 18.5:
    print(f'Seu IMC é {imc:.1f}. Classificação: PESO NORMAL.')
else:
    print(f'Seu IMC é {imc:.1f}. Classificação: ABAIXO DO PESO.')
