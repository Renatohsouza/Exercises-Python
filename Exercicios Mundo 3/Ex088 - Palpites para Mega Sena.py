
'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''

from random import randint
from time import sleep

lista = []
jogos = []

print('='*35)
print(f"{'MEGA SENA DA SORTE':^30}")
print('='*35)

num = int(input('Quantos Jogos voce deseja gerar? '))

tot = 1

while tot <= num:
    cont = 0
    while True:
        numero = randint(1,60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('~'*5,f'SORTEANDO {num} JOGOS ', '~'*5)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('~'*5,'< BOA SORTE! >', '~'*5)         
