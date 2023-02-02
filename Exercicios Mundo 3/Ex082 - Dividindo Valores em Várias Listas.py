
'''
Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.
'''

lista = []
impar = []
par = []

while True:
    num = int(input('Digite um número: '))
    lista.append(num)

    if num % 2 == 0:
        par.append(num)
    elif num % 2 == 1:
        impar.append(num)

    escolha = str(input('Deseja Continuar? [S/N]: ')).upper().strip()[0]

    if escolha == 'N':
        break

print(f'A lista completa é: {lista}')
print(f'A lita de números Pares é: {par}')
print(f'A lista de números Impares é: {impar}')
