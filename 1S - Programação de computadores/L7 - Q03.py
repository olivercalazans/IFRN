import os, sys, json

#-----------------------------------------------------------------------------------------------------------
# Questão A

year = input('Insira o ano que deseja ver (Diponiveis: 2021/2022): ')
while year != '2021' and year != '2022':
    year = input('Insira o ano, COM OS 4 DÍGITOS, que deseja ver (Diponiveis: 2021/2022): ')

DIRECTORY = os.path.dirname(os.path.abspath(__file__))
file = DIRECTORY + (f'\\cartola_fc_{year}.txt')

#-----------------------------------------------------------------------------------------------------------
# Questão B

number_position = ((3,0,4,3),(3,0,5,2),(2,2,3,3),(2,2,4,2),(2,2,5,1),(3,2,3,2),(3,2,4,1))
scheme = (('3-4-3'),('3-5-2'),('4-3-3'),('4-4-2'),('4-5-1'),('5-3-2'),('5-4-1'))
number = 0

# Escolhendo esquema tático
confirmation = False
while confirmation != True:
    print('=' * 100)
    helper0 = print('\nEsquemas táticos disponíveis: 3-4-3, 3-5-2, 4-3-3, 4-4-2, 4-5-1, 5-3-2, 5-4-1\n')
    position = input('Digite um dos esquemas tático acima: ')
    index = 0
    for counter in scheme:
        if counter == position: break
        index += 1
    index = number_position[index]
    print(f'\nEsquema tático: {index[0]} zagueiros / {index[1]} laterais / {index[2]} meias / {index[3]} atacantes\n')
    inner_conf = input('Confirma essa formação? (s = sim/n = não): ')
    inner_conf = inner_conf.lower()
    if inner_conf == 's': 
        number = index
        confirmation = True

#-----------------------------------------------------------------------------------------------------------
# Questão C

try: input_data = open(file, 'r', encoding='utf-8')
except:  print(f'ERRO...:{sys.exc_info[0]}')
else:
    # Extraindo dados do arquivo
    data = input_data.readline()
    input_data.close()
    data = json.loads(data)

    # Ordenando os jogadores por posição
    players_position = [[],[],[],[],[],[]]
    for player in data['atletas']:
        name = player['nome']
        score = player['pontos_num']
        club = player['clube_id']
        id_clubs = data['clubes']
        for index in id_clubs:
            if int(index) == club:
                id = id_clubs[index]
                club = id['nome']
        final = [name,club,score]
        position_id = player['posicao_id']
        player_class = players_position[position_id - 1]
        player_class.append(final)
    
    # Ordenando os jogadores pela pontuação (decrescente) e reduzindo a lista para 5 jogadores por posição
    #       'Gol','Lat',Zag,'Mei','Ata','Téc'
    filtered_list = [[],[],[],[],[],[]]
    for i in range(len(players_position)):
        index = players_position[i]
        list_numbers = []
        for inner in index:
            list_numbers.append(inner[2])
        list_numbers.sort(reverse=True)
        for counter in range(5):
            n = list_numbers[counter]
            for inner in index:
                if n == inner[2]:
                    helper1 = filtered_list[i]
                    helper1.append(inner)

    # Apresnetando os jogadores jogadores
    classes = ['Zagueiro','Lateral','Meias','Atacantes']
    tec = filtered_list[-1][0]
    gol = filtered_list[0][0]
    print('=' * 100)
    print(f'Escalação:\nTécnico: {tec[0]} / {tec[1]} / {tec[2]} pontos\n')
    print(f'Goleiro: {gol[0]} / {gol[1]} / {gol[2]} pontos\n')
    for n in range(4):
        if n == 0:
            cl = classes[0]
            num = number[0]
            coun = 0
            while coun < num:
                play = filtered_list[2][coun]
                print(f'{cl}: {play[0]} / {play[1]} / {play[2]} pontos')
                coun += 1
            print('\n')
        if n == 1:
            cl = classes[1]
            num = number[1]
            coun = 0
            while coun < num:
                play = filtered_list[1][coun]
                print(f'{cl}: {play[0]} / {play[1]} / {play[2]} pontos')
                coun += 1
            print('\n')
        if n > 1:
            cl = classes[n]
            num = number[n]
            coun = 0
            while coun < num:
                play = filtered_list[n + 1][coun]
                print(f'{cl}: {play[0]} / {play[1]} / {play[2]} pontos')
                coun += 1
            print('\n')