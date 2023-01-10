frase = input('Digite alguma coisa: ')
low0 = frase.lower()
low1 = low0[::-1]
number = len(low0)


counter0 = 0
counter1 = 0
while counter0 < number:
    helper0 = low0[counter0]
    helper1 = low1[counter0]
    if helper0 == helper1:
        counter1 += 1
    counter0 += 1

if counter1 == number:
    print(f'A palavra "{frase}" é um palíndromo.')
else:
    print(f'A palavra "{frase}" não é um palíndromo.')

