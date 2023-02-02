
'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

valores = []

while True:
    num = int(input('Digite um valor: '))
    
    if num not in valores:
        valores.append(num)
        print('Numero cadastrado!')
    else:
        print('Este Número ja foi cadastrado! Número nao adicionado!')

    escolha = str(input('Deseja Continuar? [S/N]: ')).upper().strip()[0]
    
    if escolha == 'N':
        break

print('='*20)
print(f'Os numeros digitados foram: {sorted(valores)}')