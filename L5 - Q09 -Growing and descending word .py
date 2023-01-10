word = input('Insira uma palavra: ')
counter0 = 0
for counter in range((len(word)) * 2):
    if counter < len(word): 
        print(word[:counter0])
        counter0 += 1
    else: 
        print(word[:counter0])    
        counter0 -= 1