from time import sleep

print('--- Seja bem vindo! ---')
print('Vamos descobrir se o numero é impar ou par?')
sleep(2)
numero = int(input('Digite um numero inteiro: '))
resutlado = numero % 2 == 0
# todo numero dividido por 2 em que o resto da divisao for 0 ele sera par,
# do contrario, se for 1, será impar!
if resutlado:
    print(f'O numero digitado é PAR!!')
else:
    print('O numero digitado é IMPAR!')
sleep(1)
print('-=-' * 12)
print('Obrigado por utilizar este programa!!')
