nome = input('Digite o nome do funcionario: ')

salario = float(input('Qual o salario do funcionario? R$ '))

novo = salario + (salario*15/100)
aumento = salario*15/100

print(f'O salario do funcionário {nome} é de {salario:.2f}')
print(f'Com o aumento de 15% no salario, ele passará a receber R$ {novo:.2f}')
print(f'O reajuste foi de R$ {aumento:.2f}!')
