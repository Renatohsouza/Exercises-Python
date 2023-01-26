from time import sleep
from random import randint
print('-=-'*20)
print('--- Seja Bem vindo Jogador! --- ')
print('-=-'*20)
sleep(1)
print('O jogo de hoje é adivinhação!')
print('-=-'*20)
sleep(1)
print('Irei pensar em um número entre 0 e 5. Você é capaz de adivinhar?!')
print('-=-'*20)
sleep(1)
jogador = int(input('Em que número eu pensei? '))
computador = randint(0, 5)
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print(f'Você é muito bom! Eu pensei no numero {jogador}!')
else:
    print(f'Você Perdeu! Eu pensei no numero {computador}!')
print('-=-'*20)
print('>>>> Obrigado por jogar comigo!! <<<<')
