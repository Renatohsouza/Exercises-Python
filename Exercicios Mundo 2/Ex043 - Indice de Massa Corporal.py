print(' === Calculadora de IMC ===')
print('-='*16)
print('Preencha as informações abaixo!')
print('-='*16)

nome = str(input('Digite seu nome: ')).strip().title()
peso = float(input('Qual o seu peso: '))
altura = float(input('Qual sua altura: '))
print('-='*16)

imc = peso / ( altura ** 2)
print(f'O IMC de {nome} é de {imc:.1f}')
print('-='*16)

if imc < 18.5:
    print('Você esta ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
    print('Você esta no PESO IDEAL!')
elif 25 <= imc < 30:
    print('Você esta com SOBREPESO')
elif 30 <= imc < 40:
    print('Você esta em estado de OBESIDADE!')
else:
    print('OBESIDADE MÓRBIDA! Cuidado!!')
