from random import randint
from time import sleep

cores = {'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'roxo': '\033[1;35m',
         'ciano': '\033[1;36m',
         'limpo': '\033[m'}

print('OLÁ, SEJA BEM VINDO JOGADOR!')
sleep(1)
print(f'O JOGO DE HOJE É {cores["ciano"]} JOKENPO! {cores["limpo"]}')
print('>>> SIGA AS INSTRUÇÕES <<<')
print(f' {cores["amarelo"]}0 = Pedra\n 1 = Papel\n 2 = Tesoura{cores["limpo"]}')

jogador = int(input('Digite sua escolha: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('-=' * 11)
print(f'Você escolheu: {cores["roxo"]}{itens[jogador]}\033[m')
print(f'Eu escolhi: {cores["ciano"]}{itens[computador]}\033[m')
print('-=' * 11)

if computador == 0:  # Computador Jogou PEDRA!
    if jogador == 0:
        print(f'{cores["amarelo"]} EMPATAMOS!!')
    elif jogador == 1:
        print(f'{cores["verde"]}VOCÊ VENCEU!!')
    elif jogador == 2:
        print(f'{cores["vermelho"]}VOCÊ PERDEU!!')
    else:
        print('JOGADA INVALIDA')
elif computador == 1:  # Computador Jogou PAPEL!
    if jogador == 0:
        print(f'{cores["vermelho"]}EU PERDEU!!')
    elif jogador == 1:
        print(f'{cores["amarelo"]} EMPATAMOS!!')
    elif jogador == 2:
        print(f'{cores["verde"]}VOCÊ VENCEU!!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:  # Computador Jogou TESOURA!
    if jogador == 0:
        print(f'{cores["verde"]}VOCÊ VENCEU!!')
    elif jogador == 1:
        print(f'{cores["vermelho"]}VOCÊ PERDEU!!')
    elif jogador == 2:
        print(f'{cores["amarelo"]} EMPATAMOS!')
    else:
        print('JOGADA INVÁLIDA!')
