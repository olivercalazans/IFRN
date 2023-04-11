# Questão 01: Listar os campus e a sua quantidade de alunos

# Questão 02: Solicitar a sigla de um campus e listar os cursos do
#             campus e a quantidade de alunos de cada curso 
#----------------------------------------------------------------------------

import requests, os

url = 'https://dados.ifrn.edu.br/dataset/d5adda48-f65b-4ef8-9996-1ee2c445e7c0/resource/00efe66e-3615-4d87-8706-f68d52d801d7/download/dados_extraidos_recursos_alunos-da-instituicao.json'

print('\nImportando dados...\n')

dados = requests.get(url).json()

#-----------------------------------------------------------
# Questão 01: Listar os campi e a sua quantidade de alunos

campi = set(map(lambda c: c['campus'], dados))
for campus in campi:
    filtro = lambda c: c['campus'] == campus
    alunos = list(filter(filtro, dados))
    qt_alunos = len(alunos)
    print(f'Campus {campus}: {qt_alunos} Alunos')
   

#------------------------------------------------------------------------
# Questão 02: Solicitar a sigla de um campus e listar os cursos do
#             campus e a quantidade de alunos de cada curso 


while True: # obtendo sigla
    sigla = input('\nInsira a sigla do campi que deseja ver: ')
    sigla = sigla.upper()
    if not sigla in campi:
        print('\nSigla incorreta. Tente uma das siglas abaixo.')
        print(campi)
    else:
        break

aux = list()
print(100 * '=')
filtro = lambda c: c['campus'] == sigla
campi_sigla = list(filter(filtro, dados)) # reduzindo a lista pelo campi escolhido 
cursos = set(map(lambda c: c['curso'], campi_sigla)) # obtendo os cursos do campi escolhido
for curso in cursos:
    filtro_in = lambda c: c['curso'] == curso
    alunos = list(filter(filtro_in, campi_sigla)) # contabilizando a quantidade de alunos
    aux = alunos
    quant_alunos = len(alunos)
    print(f'{curso} --- {quant_alunos} alunos')
print(100 * '=')

#-----------------------------------------------------------------------------------------------
# Gerar arquivo do campus escolhido

arquivo = input('\nCriar um arquivo do campi? (yes/no): ').lower()
while True:
    if arquivo != 'yes' or arquivo != 'no':
        arquivo = input('\nResposta incompativel. Escreva (yes/no): ').lower()
    else:
        break

if arquivo == 'yes':

   