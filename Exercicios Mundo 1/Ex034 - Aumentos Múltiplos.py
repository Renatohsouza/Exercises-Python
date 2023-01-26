from time import sleep
print('Seja Bem vindo!')
sleep(1)
print('-=-' * 15)
print('**** CALCULO DE AUMENTO DE SALARIO ****')
salario = float(input('Digite o Valor do salario R$: '))
# Simplificado
if salario <= 1250:
    novo = salario + (15 * salario / 100)
else:
    novo = salario + (10 * salario / 100)
print(f'Quem ganhava {salario}, passa a recer o valor de R$ {novo:.2f}')


# Meu raciocinio #

## Esta correto tambem, mas existe uma forma mais simplificada acima!

'''calculo1 = (10*salario)/100
calculo2 = (15*salario)/100
if salario >= 1250.00 != calculo1:
    print(f'Quem ganhava {salario}, com o aumento de 10%, Passou a receber R${calculo1+ salario:.2f}')
else:
    print(f'Quem ganhava {salario}, com o aumento de 15%,  Passou a receber R${calculo2 + salario:.2f} ')'''
