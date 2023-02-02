
'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''
valores = []
maior = menor = 0

for n in range (0,5):
    valores.append(int(input(f'Digite um número na posição {n}: ')))
    
    if n == 0:
        maior = menor = valores[n]
    else:
        if valores[n] > maior:
            maior = valores[n]
        if valores[n] < menor:
            menor = valores[n]

print(f'Voce digitou os valores {valores}')
print(' ')
print(f'O Maior valor digitado foi {maior} e ele está na posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O Menor valor foi {menor} e ele está na posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
print()

# i = Indice # v = Valor