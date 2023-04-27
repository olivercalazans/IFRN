# Esse código faz uma lista de todos os campis do IFRN e mostra a quantidade de alunos.
# Também é possível escolher um campi para poder gerar uma lista com todos os cursos e a quantidade de alunos.
# Caso deseje, esse código criará um arquivo com as informações do campi escolhido.
#----------------------------------------------------------------------------

import requests, os, sys

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
print('\n' + 100 * '=')
   

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

print('\n' + 100 * '=')
aux = list()
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
# Gerar arquivo do campus escolhido.

# Obtendo permissão para criar o arquivo.
arquivo = input('\nCriar um arquivo do campi? (yes/no): ').lower()
while True:
    if arquivo != 'yes' and arquivo != 'no':
        arquivo = input('\nResposta incompativel. Escreva (yes/no): ').lower()
    else:
        break

if arquivo == 'yes':

    DIRETORIO  = os.path.dirname(os.path.abspath(__file__))
    DIRETORIO += '\\dados_ifrn\\'
    
    # Criando pasta para facilitar a localização do arquivo.
    try:
        os.mkdir(DIRETORIO)
    except FileExistsError:
        print('\nO diretóro já existe.\n')
    except:
        print(f'ERRO...:{sys.exc_info()[0]}')
    else:
        print(f'\nDiretório criado com sucesso!!!\n') 
    
    # Gerando arquivo.
    try:
        DadosParaEscrever = open(DIRETORIO + f'dados_campi({sigla}).txt', 'w', encoding='utf-8')
    except:
        print(f'ERRO...:{sys.exc_info[0]}')
    else:
        DadosParaEscrever.write('curso,quantidade_de_alunos')
        for curso in cursos:
            DadosParaEscrever.write(f'{curso} --- {quant_alunos} alunos\n')
        DadosParaEscrever.close()
        print('Arquivo criado com sucesso!!!')
        print('\n' + 100 * '=')
        print('\nFIM\n')
else:
    print('\nFIM\n')
    