
'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort()). 
No final, mostre a lista ordenada na tela
'''

lista = []

for c in range (0,5):
    num = int(input('Digite um Valor: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Item adicionado no final da lista.')
    else:
        posição = 0
        while posição < len(lista):
            if num <= lista[posição]:
                lista.insert(posição, num)
                print(f'Item Adicionado na posição {posição}!')
                break
            posição += 1
print(' ')
print(f'Os Valores digitados foram: {lista}')