nome = str(input('Qual seu nome: '))
if nome == 'Wesley':
    print('Olá Wesley, seu nome é muito bonito')
elif nome == 'Maria' or nome == 'João':
    print(f'Olá {nome}, seu nome é bem comum no Brasil!')
else: 
    print(f'Olá {nome}')