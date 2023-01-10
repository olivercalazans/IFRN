number = int(input('Informe o número inicial: '))
helper, helper1 = 0, 0
for counter in range(15):
    print(number, end=',')
    helper1 = number
    number += helper
    helper = helper1
