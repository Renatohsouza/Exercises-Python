
'''
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
'''

from random import randint

print('=-'*22)
print(f"{'Bem Vindo Jogador!':^40}")
print(f"{'-- Vamos jogar PAR ou IMPAR! -- ':^40}")
print('=-'*22)

vitoria = 0

while True:
    n = int(input('Escolha um número jogador: '))
    computador = randint(0,n) # <-- Para roletar números até o numero que foi digitado pelo Jogador.
    soma = n + computador
    escolha = ' '

    while escolha not in 'PI': # < -- Inseri outro while, conforme resolução do professor Guanabara, esta foi a única alteração.
        escolha = str(input('PAR OU IMPAR? [P/I]: ')).upper().strip()[0]
    print('='*22)

    print(f'O computador escolheu: {computador}')
    print(f'Você escolheu: {n}')
    print('='*22)

    if escolha == 'P':
        if soma % 2 == 0:
            print(f'{soma} é PAR! Você venceu!')
            vitoria += 1
        else:
            print(f'{soma} é IMPAR! Você perdeu!')
            break
    if escolha == "I":
        if soma % 2 == 1:
            print(f'{soma} é IMPAR! Você venceu!')
            vitoria += 1
        else:
            print(f'{soma} é PAR! Você perdeu!')
            break

print('='*22)
print(f'>> Você venceu {vitoria} vezes!')
