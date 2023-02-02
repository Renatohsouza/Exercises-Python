from time import sleep
from emoji import emojize

print(f'{" LOJA SWEET VON ":=^40}')
sleep(1)

preco = float(input('Qual o valor da compra: R$ '))

print(emojize("Formas de Pagamento :dollar:", language='alias')) #Testando a aplicação de emojis
print(
'''[ 1 ] - Dinheiro a vista
[ 2 ] - Débito a vista
[ 3 ] - 2x no Cartão
[ 4 ] - 3x ou mais no Cartão''')
print('-='*20)

pagamento = int(input('Qual a opção de Pagamento? '))
print('-='*20)

if pagamento == 1:
    total = preco - (preco * 10 / 100)
elif pagamento == 2:
    total = preco - (preco * 5 / 100)
elif pagamento == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R$ {parcela:.2f} sem juros!')
elif pagamento == 4:
    total = preco + (preco * 20 / 100)
    total_parcelas = int(input('Em quantas parcelas você gostaria? '))
    parcela = total / total_parcelas
    print(f'Sua compra será parcelada em {total_parcelas}x de R$ {parcela:.2f} com juros!')
else:
    total = preco
    print('Opção Inválida! Tente Novamente!')
    
print(f'Sua compra de R$ {preco:.2f}, vai custar R$ {total:.2f} no final')