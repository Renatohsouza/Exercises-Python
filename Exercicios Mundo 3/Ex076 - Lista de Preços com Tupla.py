
'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabula
'''

itens = 'Estojo',8,'Caderno',20,'Lápis',1,'Caneta',3,'Pasta', 12,'Estilete',6,'Cola',3,'Tesoura',5,'Mochila',80

print('=' * 40)
print(f"{'- ITENS -':^40}")
print('=' * 40)

for pos in range (0, len(itens)): # <-- se a posição estiver entre 0 e o final da tupla. verificar a posição entre Par e Impar.
    if pos % 2 == 0:
        print(f'{itens[pos]:.<30}', end='')
    else:
        print(f'R${itens[pos]:>7.2f}')
print('=' * 40)
