var = '0123456789'

number =  len(var)
aux = (number * 2)

number_of_repetitions = 1
position = 0
while number_of_repetitions <= aux:
    if number_of_repetitions <= number:
        print(var[:position])
        position += 1
        number_of_repetitions += 1
    elif number_of_repetitions > number:
        print(var[:position])
        position -= 1
        number_of_repetitions += 1

    


