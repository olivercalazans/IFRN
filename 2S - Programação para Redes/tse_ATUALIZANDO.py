'''
    O TSE divulga na sua página oficial um webservice que fornece os dados 
    das apurações das eleições realizadas no Brasil.
    O fragmento de código a seguir monta um dicionário (dados_retorno) com o 
    resultado das eleições do ano de 2022 no 1º turno para Presidente.
    Com base na documentação da API contida na URL 
    https://www.tse.jus.br/eleicoes/eleicoes-2022/interessados-na-divulgacao-de-resultados-2022
    Pede-se que seja desenvolvido um programa que solicite ao usuário o 
    ano da eleição, tipo de eleição (estadual, nacional) e o cargo eletivo 
    e o programa  deverá montar um dicionário {k:v} no seguinte formato:
    {
        num_candidato: { 'nome ': nome_candidato, 'partido': nome_partido, 
                         'votos': quantidade_votos, 
                         'percentual': percentual_votos},
        num_candidato: { 'nome ': nome_candidato, 'partido': nome_partido, 
                         'votos': quantidade_votos, 
                         'percentual': percentual_votos},
        ...
    }
    
    O dicionário deverá ser ordenado de forma decrescente pela quantidade de
    votos que o candidato obteve.
    Em seguida, deverá ser gerado um arquivo (resultados.txt) onde na 
    primeira linha deverá constar a seguinte string:
        numero;nome,partido;quantidade_votos;percentual_votos
    Da segunda linha em diante deverão constar os dados correspondentes de
    cada candidato
'''


import requests, sys, os


# Obtendo o ano.
while True:
    try: 
        ano = int(input('Digite o ano da eleição: '))
    except ValueError:
        print('DIGITE APENAS NÚMEROS.\n')
    except:
        print(f'ERRO...:{sys.exc_info()[0]}')
    else:
        break


# Obtendo a sigla do estado.
SIGLA = ['ac','al','ap','am','ba','ce','df','es','go','ma','mt','ms','mg','pa',
         'pb','pe','pi','pr','rj','rn','ro','rr','rs','sp','to','sc','se','br']
while True:
        sigla = input('\nDigite a sigla do estado ("br" se for nacional): ').lower()
        if not sigla in SIGLA:
             print('SIGLA INCORRETA.')
        else:
             break


# Obtendo o cargo.
while True:
    try:
        print('1: Presidente.\n')
        cargo = input('\nDigite o cargo o código do cargo: ')
    except ValueError:
        print('DIGITE APENAS NÚMEROS.\n')
    except:
        print(f'ERRO...:{sys.exc_info()[0]}')
    else:
        break


# Obtendo o ID da eleição.
while True:
    try: 
        id_eleicao = int(input('\nDigite o ID da eleição: '))
    except ValueError:
        print('DIGITE APENAS NÚMEROS.\n')
    except:
        print(f'ERRO...:{sys.exc_info()[0]}')
    else:
        break



url  = 'https://resultados.tse.jus.br/oficial/'
url += f'ele{ano}/{id_eleicao}/dados-simplificados/{sigla}/'
url += f'{sigla}-c{cargo}-e000544-r.json'


dados_retorno = requests.get(url).json() # Buscando dados na rede.

candidatos = dados_retorno['cand'] # Separando as informações importantes.

# Pegando apenas as informações pedidas (nome, partido, n° de votos e porcentagem).
dicionario = dict()
for i in candidatos: 
    d = [i['n'],i['nm'],i['cc'],i['vap'],i['pvap']]
    dicionario[d[0]] = {'nome': d[1],'partido': d[2],'votos': d[3],'porcentagem': d[4],}

# Apresentando os dados.
for i in dicionario:
    print(f'{i}: {dicionario[i]}')

DIRETORIO  = os.path.dirname(os.path.abspath(__file__))
DIRETORIO += '\\pasta_tse\\'

# Criando pasta para o arquivo.

try:
    os.mkdir(DIRETORIO)
except FileExistsError:
    print('O diretóro já existe\n')
except:
    print(f'ERRO...:{sys.exc_info()[0]}')
else:
    print(f'Diretório {DIRETORIO.upper()} criado com sucesso!!!\n') 


# Criando arquivo.
try:
    dados_escrita = open(DIRETORIO + 'dados_tse.txt', 'w', encoding='utf-8')
except:
    print(f'ERRO...:{sys.exc_info[0]}')
else:
    dados_escrita.write('numero;nome,partido;quantidade_votos;percentual_votos\n')
    for i in dicionario:
        dados_escrita.write(f'{i}: {dicionario[i]}\n')
    dados_escrita.close()
    print('Arquivo criado com sucesso!!!')
