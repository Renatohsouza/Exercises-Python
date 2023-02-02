
'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre: 
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.                                                                          
C) Se o valor 5 foi digitado, se está ou não na lista e quantas vezes ele aparece.
'''

lista =[]

cont = cont5 = 0

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    print('Número Adicionado!')
    cont += 1

    if num == 5:
        cont5 += 1

    escolha = str(input('Deseja continar? [S/N]: ')).strip().upper()[0]

    if escolha == 'N':
        break

lista.sort(reverse = True)

print('=' * 35)
print(f'Você digitou {cont} números!')
print(f'Os valores em ordem decrescente: {lista}')
if 5 in lista:
    print(f'O número 5 foi inserido! você digitou ele: {cont5} vezes!')
else:
    print('O número 5 não foi digitado nenhuma vez!')
