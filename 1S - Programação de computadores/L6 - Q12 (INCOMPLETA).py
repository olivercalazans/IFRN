import random 

quantity = int(input('Insira um número entre 7 e 60: '))
numbers = random.sample(range(1, 60), quantity)
numbers.sort()

six = []
for i in numbers:
    number = random.sample((numbers), 6)
    print(numbers)
    print(number)
    break