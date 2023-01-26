print('Bem vindo ao Sitema de Multas Online (SMO)!')
velocidade = float(input('Qual a velocidade em que passou no radar? '))
multa = 7*(velocidade-80)
if velocidade <= 80:
    print('Você não foi multado!')
else:
    print(f'Você ultapassou o limite da via que é de 80km/h! Você deve pagar uma multa de R${multa:.2f}')