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
    helper += reason
if reason > 0: print(f'\nA progressão é crecente.\nA soma dos valores é {sum}.\nE o enezimo número é {number}.')
elif reason < 0: print(f'\nA progressão é decrecente.\nA soma dos valores é {sum}.\nE o enezimo número é {number}.')
print(100 * '=')