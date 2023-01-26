from time import sleep
from datetime import date

print('Ola, Seja Bem Vindo!')
print('Hoje iremos descobrir se um ano é Bissexto ou não!')
print('-=-' * 20)
sleep(1)

ano = int(input('Qual ano gostaria de analizar? Digite 0 para analizar o ano atual: '))
print('VERIFICANDO...')
sleep(1)

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano}, é Bissexto! ')
else:
    print(f'O ano de {ano}, é um ano comum!')
sleep(1)

print('-=-' * 20)
print('>>> Obrigado e Volte sempre que tiver duvidas! <<<')
