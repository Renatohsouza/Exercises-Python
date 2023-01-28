
'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:   
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''
lista = [] # < -- Lista temporária

pessoas = [] # <-- Lista Principal 

contPessoas = maior = menor = 0

while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        maior = menor = lista[1]
    else: 
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]

    pessoas.append(lista[:]) # <-- Pegando a Lista temporária e fazendo uma cópia dentro de Pessoas.
    lista.clear() # <-- Limpando a lista temporária.
    contPessoas += 1

    desejo = str(input('Deseja Continuar? [S/N]: ')).upper().strip()[0]

    if desejo == 'N':
        break
    
print('~'*30)  
print(f'Foram cadastrados {contPessoas} Pessoas!')
print(' ')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de  {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()
