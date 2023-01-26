produto = float(input('Qual o valor do produto? R$'))
novo = produto - (produto*5/100)
desconto = produto*5/100
print(f'O Valor do produto é de {produto:.2f} e na promoção com o desconto de 5% é de {novo:.2f}!')
print(f'Você obteve um desconto de R${desconto:.2f}!')
