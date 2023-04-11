frase = input('Digite uma frase: ')
aux0 = frase.lower()
antiga = input('Qual palavra você deseja substituir: ')
aux1 = antiga.lower()
nova = input('Qual a palavra nova: ')
aux2 = nova.lower()

print(f'Frase {frase}. Palavra que será substituida: {antiga}. Nova palavra: {nova}.')

frase_nova = frase.replace(antiga, nova)

print(f'Frase nova: {frase_nova}.')