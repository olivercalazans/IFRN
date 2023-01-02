cpf = input('Informe um CPF: ')
if len(cpf) > 11:
    print('Quantidade de números inseridas inválida, um CPF deve conter 11 digitos.')
else:
    helper0 = 0
    helper1 = 10
    amount = 0
    while helper1 >= 2:
        amount += int(cpf[helper0]) * helper1
        helper0 += 1
        helper1 -= 1
    if amount % 11 >= 10:
        number0 = 0
    else:
        number0 = int('11') - (amount % 11)
    helper0 = 1
    helper1 = 10
    amount = 0
    while helper1 >= 2:
        amount += int(cpf[helper0]) * helper1
        helper0 += 1
        helper1 -= 1
    if int('11') - amount % 11 >= 10:
        number1 = 0
    else:
        number1 = int('11') - (amount % 11)
    cpf2 = ''
    cpf2 += cpf[:9] + str(number0) + str(number1)
    if cpf == cpf2:
        print('CPF válido!')
    else:
        print('CPF inválido!')