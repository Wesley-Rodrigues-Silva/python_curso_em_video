from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(0.7)
print('KEN')
sleep(0.7)
print('PO!!!')
print('-=' * 11)
print(f'Computador jogou {itens[computador]}')
print(f'Você jogou {itens[jogador]}')
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('EMPATE! Os dois fizeram a mesma jogada')
    elif jogador == 1:
        print('Você venceu!')
    elif jogador == 2:
        print('O computador venceu!')
    else:
        print('Jogada inválida!')
if computador == 1:
    if jogador == 0:
        print('O computador venceu!')
    elif jogador == 1:
        print('EMPATE! Os dois fizeram a mesma jogada')
    elif jogador == 2:
        print('Você venceu!')
    else:
        print('Jogada inválida!')
if computador == 2:
    if jogador == 0:
        print('Você venceu!')
    elif jogador == 1:
        print('O computador venceu!')
    elif jogador == 2:
        print('EMPATE! Os dois fizeram a mesma jogada')
    else:
        print('Jogada inválida!')