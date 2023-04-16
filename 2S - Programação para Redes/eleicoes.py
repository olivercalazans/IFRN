'''
    Esse código pega os dados da eleição que for escolhida e faz um resumo dos candidatos.
    É possível criar um arquivo com as informações que foram mostradas.
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
print(140 * '-')

# Obtendo comando para criação de um arquivo.
while True:
    criacao_arq = input('\nDeseja criar um arquivo com essas informações? (yes/no): ').lower()
    if criacao_arq != 'yes' and criacao_arq != 'no':
        print('Comando não entendido. Tente novamente.')
    else:
        break

if criacao_arq == 'yes': 
    # Criando pasta para o arquivo.
    DIRETORIO  = os.path.dirname(os.path.abspath(__file__))
    DIRETORIO += '\\pasta_tse\\'

    try:
        os.mkdir(DIRETORIO)
    except FileExistsError:
        print('\nO diretóro já existe.\n')
    except:
        print(f'ERRO...:{sys.exc_info()[0]}')
    else:
        print(f'\nDiretório criado com sucesso!!!\n') 

    # Criando arquivo.
    try:
        dados_escrita = open(DIRETORIO + f'dados_tse_({sigla},{ano}).txt', 'w', encoding='utf-8')
    except:
        print(f'ERRO...:{sys.exc_info[0]}')
    else:
        dados_escrita.write('numero;nome,partido;quantidade_votos;percentual_votos\n')
        for i in dicionario:
            dados_escrita.write(f'{i}: {dicionario[i]}\n')
        dados_escrita.close()
        print('Arquivo criado com sucesso!!!')
        print('\nIsso é tudo.')
else:
    print('\n' + 140 * '-')
    print('\nIsso é tudo.')
