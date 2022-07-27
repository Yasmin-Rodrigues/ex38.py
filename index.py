from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura' )
computador = randint(0,2)
print('Suas opções:\n[0]PEDRA\n[1]PAPEL\n[2]TESOURA')
jogador =int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('==' *12)
print(f'Computador jogou: {itens[computador]}')
print(f'Jogador jogou: {itens[jogador]}')
print('==' *12)
if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador ==1:
        print('Você venceu!')
    elif jogador ==2:
        print('Você perdeu!')
    else:
        print('Jogada inválida!')
elif computador == 1:
    if jogador == 0:
        print('Computador venceu!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Você venceu!')
    else:
        print('Jogada inválida!')
elif computador ==2:
    if jogador == 0:
        print('Você venceu!')
    elif jogador == 1:
        print('Você perdeu!')
    elif jogador == 2:
        print('Empate!')
    else:
        print('Jogada inválida')
        