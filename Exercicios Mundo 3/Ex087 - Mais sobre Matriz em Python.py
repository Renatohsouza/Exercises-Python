
'''
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha
'''
somaPar = soma3 = maior = 0

matriz = [[0,0,0],[0,0,0],[0,0,0]]

for linha in range (0,3):
    for coluna in range (0,3):
        matriz[linha][coluna]= int(input(f'digite um valor para a posição [{linha},{coluna}]: '))
print('~'*40)

for linha in range (0,3):
    for coluna in range (0,3):
        print(f'[{matriz[linha][coluna]:^4}]', end='')
        
        if matriz[linha][coluna] % 2 == 0:
            somaPar += matriz[linha][coluna]
    print()

print('~'*40)
print(f'A soma de todos valores pares : {somaPar}')

for linha in range (0,3):
    soma3 += matriz[linha][2]
print(f'A soma dos valores da 3º Coluna: {soma3}')

for coluna in range(0,3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'O maior valor da 2º Linha é: {maior}')