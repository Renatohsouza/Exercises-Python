
'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
'''



numero = (int(input('Digite um número: ')),
          int(input('Digite outro número: ')),
          int(input('Digite mais um número: ')),
          int(input('Digite o ultimo número: ')))

print('=' * 40)
print(f'você digitou os valores: {numero}')
print('=' * 40)
print(f'O Valor 9 apareceu {numero.count(9)} vezes!')
print('=' * 40)

if 3 in numero:
    print(f'O valor 3 apareceu {numero.index(3)+1}º posição!')
else:
    print('O número 3 não apareceu nenhuma vez!')
print('=' * 40)

print(f'Os valores pares digitados foram: ', end='')
for n in numero:
    if n % 2 ==0:
        print(n, end=' ')
