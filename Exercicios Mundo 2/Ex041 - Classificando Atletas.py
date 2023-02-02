from datetime import date
from time import sleep

print(' === Classificação de Idade dos Atletas ===')
print('-='*18)
sleep(1)

nome = str(input('Nome do atleta: ')).strip().title()
nasc = int(input('Ano de nascimento do Atleta: '))

idade = date.today().year - nasc

print(f'O Atleta {nome} tem {idade} anos!')
print('-='*18)

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')
    