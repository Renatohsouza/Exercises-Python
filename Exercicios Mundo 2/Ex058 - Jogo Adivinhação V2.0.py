from random import randint

# Minha resolução ##
'''
        jogador = int(input('Que número eu pensei entre 0 e 10?: '))
        computador = randint(0,10)

        tentativas = 0

        while jogador != computador:
            jogador = int(input('Você Errou!.. Tente outro número: '))
            tentativas += 1
            
        print(f'Parabéns Você acertou com um total de {tentativas+1} tentativas!') ''' 
        # Utiizei o +1 para somar com a primeira tentativa, 
        # tendo em vista que ele contava so as tentativas dentro do while,
        # Devido eu ter feito a condição ja no próprio while.

# Resolução Guanarabara ##

print('Olá Jogador, eu sou seu computador!')
print('Eu pensei em um número entre 0 e 10.')
print('Sera que você consegue adivinhar qual eu escolhi? ')

computador = randint(0,10)

acertou = False
tentativas = 0

while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Um pouco mais... Tente novamente!')
        elif jogador > computador:
            print('Um pouco menos... Tente novamente!')
        
print(f'Parabéns, você acertou! Com um total de {tentativas} tentativas!')

