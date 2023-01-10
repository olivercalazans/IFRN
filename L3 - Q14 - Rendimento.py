valor_investido = float(input('Informe o valor investido: '))
porcent = float(input('Informe o rendimento mensal, sem o sinal (%): '))
aux = input(f'Valor invstido: {valor_investido}, redimento: {porcent}%. Valores corretos? (S/N): ')
aux = aux.upper()

porcent /= 100
ano =0
montante = 0
rendimento = 0

while aux != 'N':
    mes = 0
    while mes < 12:
        montante += valor_investido
        rendimento = montante * porcent
        montante += rendimento
        rendimento = 0 
        mes += 1
    
    ano += 1
    print(f'Ao final de {ano}, você receberá R${montante:.2f}.')
    aux = input('Deseja calcular o redimento de mais 1 ano? (S/N): ')
    aux = aux.upper()
