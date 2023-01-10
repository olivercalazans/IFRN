first = int(input('Informe o número inicial: '))
repetition = int(input('Quantos números deseja ver?  '))
reason = int(input('Informe a razão: '))
position = int(input('Qual a enezima posição: '))
number,sum, helper= 0, 0, first
print(100 * '=')
for counter in range(repetition):
    print(helper, end=';')
    sum += helper
    if counter == position: number += helper
    helper *= reason
if reason == 1: print(f'\nProgreção geometrica constante.\nA soma dos valores é {sum}.\nO valor enésimo é {number}.')
elif first > 0 and reason > 0: print(f'\nProgreção geomerica crescente.\nA soma dos valores é {sum}.\nO valor enésimo é {number}.')
elif first < 0 and reason > 0: print(f'\nProgreção geometrica decrecentes.\nA soma dos valores é {sum}.\nO valor enésimo é {number}.')
else: print(f'\nProgreção geometrica oscilante.\nA soma dos valores é {sum}.\nO valor enésimo é {number}.')
print(100 * '=')