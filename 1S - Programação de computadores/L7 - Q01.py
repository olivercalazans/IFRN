import os, sys, statistics, time

start = time.time()

# Diretórios
DIRECTORY      = os.path.dirname(os.path.abspath(__file__))
ANP_DATAFILES  = DIRECTORY + '\\serie_historica_anp\\'
STATISTIC_DATA = DIRECTORY + '\\dados_estatisticos\\'

print('=' * 100 + '\n')

# Lista dos arquivos  
try: files = os.listdir(ANP_DATAFILES)
except:
    print(f'ERRO NA LOCALIZAÇÃO DO ARQUIVO (serie_historica_anp).... {sys.exc_info()[0]}')
    sys.exit()

#--------------------------------------------------------------------------------------------------------------------------------------------
# Item A

print('Criando o diretório...')
try: os.mkdir(STATISTIC_DATA)
except FileExistsError: print('O diretóro já existe\n')
except: print(f'ERRO...:{sys.exc_info()[0]}')
else: print(f'Diretório {STATISTIC_DATA.upper()} criado com sucesso!!!\n') 


#--------------------------------------------------------------------------------------------------------------------------------------------
# Item B

print('Lendo arquivos...')
read_data = []
for file in files:
    try: data_input = open(ANP_DATAFILES + file, 'r', encoding='utf-8')
    except: 
        print(f'ERRO...:{sys.exc_info[0]}')
        sys.exit()
    else:
        header = data_input.readline()
        while True:
            line  = data_input.readline()[:-1]
            if not line: break
            line = line.split(';')
            read_data.append([line[0], line[1], line[10], line[11], float(line[12].replace(',', '.')), line[15]])
        print(f'Arquivo lido: {file}')
        data_input.close()
print('Arquivos lidos com sucesso!!!\n')

#--------------------------------------------------------------------------------------------------------------------------------------------
# Item C

print('Escrevendo arquivo "SERIE_HISTORICA_ANP.TXT"...')
try: data_output = open(STATISTIC_DATA + 'serie_historica_anp.txt', 'w', encoding='utf-8')
except: print(f'ERRO...:{sys.exc_info[0]}')
else: 
    data_output.write('Região;Estado;Produto;Data;Valor;Bandeira\n')
    for data in read_data:
        data_output.write(f'{data[0]};{data[1]};{data[2]};{data[3]};{data[4]};{data[5]}\n')
    data_output.close() 
    print('Arquivo escrito com sucesso!!!\n')

#--------------------------------------------------------------------------------------------------------------------------------------------
# Item D - Parte I

print('Gerando arquivo "BANDEIRA x PRODUTO x ANO x VALOR MÉDIO VENDA x QUANTIDADE DE POSTOS" ...')

ban_pro_ano = set(map(lambda p: (p[5], p[2], p[3][6:]), read_data))

try: output_data = open(STATISTIC_DATA + 'bandeira_produto_ano.txt', 'w', encoding='utf-8')
except: print(f'ERRO...: {sys.exc_info()[0]}\n')
else:
    output_data.write('BANDEIRA;PRODUTO;ANO;VALOR_MEDIO_PRODUTO;QUANTIDADE_POSTOS\n')
    for data in ban_pro_ano:
        filter1 = list(filter(lambda f : f[-1] == data[0] and f[2] == data[1] and f[3][6:] == data[2], read_data))
        values = list(map(lambda v : v[4], filter1))
        average = statistics.mean(values)
        number = len(values)
        output_data.write(f'{data[0]};{data[1]};{data[2]};{average:.2f};{number}\n')
    output_data.close()
    print('Arquivo escrito com sucesso!!!\n')

print('Gerando arquivo "PRODUTO x REGIÃO x ANO x VALOR MÉDIO VENDA x QUANTIDADE DE POSTOS" ...')

pro_reg_ano = set(map(lambda p: (p[2], p[0], p[3][6:]), read_data))

try: output_data = open(STATISTIC_DATA + 'produto_regiao_ano.txt', 'w', encoding='utf-8')
except: print(f'ERRO...: {sys.exc_info()[0]}\n')
else:
    output_data.write('PRODUTO;REGIAO;ANO;VALOR_MEDIO_PRODUTO;QUANTIDADE_POSTOS\n')
    for data in pro_reg_ano:
        filter1 = list(filter(lambda f : f[2] == data[0] and f[0] == data[1] and f[3][6:] == data[2], read_data))
        values = list(map(lambda v : v[4], filter1))
        average = statistics.mean(values)
        number = len(values)
        output_data.write(f'{data[0]};{data[1]};{data[2]};{average:.2f};{number}\n')
    output_data.close()
    print('Arquivo escrito com sucesso!!!')

end = time.time()
print(f'O tempo total de execução em Minutos foi de -> {((end-start)/60):.2f}')