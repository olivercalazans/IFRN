valor = float(input('Informe o valor a ser sacado: '))

if valor <= 0:
    print('Não é possível sacar valores negativos.')
else: 
        #100
        cent = valor // 100
        rest_cent = valor % 100
        #50
        cinq = rest_cent // 50
        rest_cinq = rest_cent % 50
        #20
        vin = rest_cinq // 20
        rest_vin = rest_cinq % 20
        #10
        dez = rest_vin // 10
        rest_dez = rest_vin % 10
        #5
        cinc = rest_dez // 5
        rest_cinc = rest_dez % 5
        #2
        dois = rest_cinc // 2
        rest_dois = rest_cinc % 2 
        #1
        um = rest_dois // 1
        rest_um = rest_dois % 1
        #0,50
        cent50 = rest_um // 0.5
        rest_cent50 = rest_um % 0.5
        #0,25
        cent25 = rest_cent50 // 0.25
        resr_cent25 = rest_cent50 % 0.25
        #0,10
        cent10 = resr_cent25 // 0.1
        rest_cent10 = resr_cent25 % 0.1
        #0,05
        cent05 = rest_cent10 // 0.05
        rest_cent05 = rest_cent10 % 0.05
        #0,01
        cent01 = rest_cent05 // 0.01

        print(f'Você receberá {cent} notas de 100; {cinq} notas de 50; {vin} notas de 20; {dez} notas de 10; {cinc} notas de 5; {dois} notas de 2; \n{um} moedas de 1; {cent50} moedas de 0.50; {cent25} moedas de 0.25; {cent10} moedas de 0.10; {cent05} moedas de 0.05 e {cent01} moedas de 0.01.')
