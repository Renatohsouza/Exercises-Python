produto = float(input('Digite o valor de um produto: R$ '))

valor1 = produto + (produto*5/100)
valor2 = produto - (produto*7/100)
desconto = valor2 - produto
juros = valor1 - produto

print(f'O valor do produto com desconto a vista é de R$ {valor2:.2f}\nO valor do produto com juros é de R$ {valor1}!')

print(f'O valor do desconto é de R$ {desconto:.2f}\nO Valor do juros é de R$ {juros}!')
