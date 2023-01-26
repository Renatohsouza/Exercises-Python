
'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato. 
'''
print('='*40)
print(f"{' Seja bem vindo ao Mercadinho ':-^40}")
print('='*40)

soma = produtos1k = menor = cont = 0
maisBarato = ''

while True:

    produto = str(input('Digite o nome do produto: ')).strip()
    preço = float(input('Preço do produto: R$ '))
    print('='*40)
    cont += 1
    soma += preço

    if preço >= 1000:
        produtos1k += 1

    if cont == 1 or preço < menor: # Simplificação do código para verificar qual o menor preço e qual o nome do menor preço.
        menor = preço
        maisBarato = produto         

    

print(F"{' FIM DO PROGRAMA ':-^30}")
print('='*40)
print(f'>>> Total da compra R${soma:.2f}!')
print(f'>>> Foram cadastrados {produtos1k} produtos acima de R$ 1.000,00!')
print(f'>>> O produto mais barato foi {maisBarato} e custa R${menor:.2f}!')