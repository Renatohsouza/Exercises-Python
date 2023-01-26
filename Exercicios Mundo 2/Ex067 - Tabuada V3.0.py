
'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. 
'''
print('='*42)
print(f"{'Seja Bem Vindo a sua Tabuada V.3':^40}")
print('='*42)
print('Digite qualquer número negativo para sair!')
print('='*42)

1

while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    print('~'*40)
    if n < 0:
        break
    for tabuada in range (1,11):
        print(f'{n} X {tabuada} = {n*tabuada}')
    print('~'*40)

print('~ Obrigado por utilizar a Tabuada! ~')
print('>> FIM DO PROGRAMA! <<')