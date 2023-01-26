
'''
Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
'''
soma = contNum = 0

print(f"{'Seja Bem vindo!':^40}")
print('~'*40)
print('>> Digite "999" para sair do programa! <<')
print('~'*40)

while True:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break  
    soma += n
    contNum += 1    

print('~'*40)
print(f'>>> Você digitou {contNum} números!')
print(f'>>> A soma dos números digitados foi {soma}!')
print('~'*40)
print('>> FIM DO PROGRAMA! <<')