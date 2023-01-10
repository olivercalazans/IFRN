DEFAULT_PASSWORD = 'swordfish'
password = input('Digite a senha: ')
for counter in range(1000000):
    if password == DEFAULT_PASSWORD: 
        print('Welcome back.')
        break
    else: password = input('Senha incorreta. Tente novamente: ')