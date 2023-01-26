from datetime import date

contmaior = 0
contmenor = 0

for pessoal in range (1,8):
    ano = int(input(f'Qual ano de nascimento da {pessoal}º pessoa? '))
    atual = date.today().year
    idade = atual - ano
    
    if idade >= 18:
        contmaior += 1
    else:
        contmenor += 1

print('-='*20)
print(f'{contmaior} pessoa(s) MAIORES de idade!')
print(f'{contmenor} pessoa(s) MENORES de idade!')
