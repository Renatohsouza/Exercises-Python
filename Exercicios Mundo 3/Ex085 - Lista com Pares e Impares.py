
'''
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''
numeros = [[],[]] # <-- Uma lista dentro de outra lista --> numeros = [[par],[impar]] 

valor = 0

for v in range (1,8):
   valor = int(input(f'Digite {v}º o número: '))
   
   if valor % 2 == 0:
    numeros[0].append(valor)
   if valor % 2 == 1:
    numeros[1].append(valor)

sorted(numeros[0])
sorted(numeros[1])

print(f'Os números pares digitados foram: {numeros[0]}')
print(f'Os números impares foram: {numeros[1]}')