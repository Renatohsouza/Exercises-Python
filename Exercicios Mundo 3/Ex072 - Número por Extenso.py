
'''
 Crie um programa que tenha uma Tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado 
 (entre 0 e 20) e mostrá-lo por extenso.
'''

contagem = 'Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','vinte'

# Minha solução sem o "continue" #


print('='*45)
numero = int(input('Digite um número entre 0 e 20: '))
print('='*45)

while numero not in range(0,21):
    numero = int(input('Tente Novamente. Digite um número entre 0 e 20: '))
    
print('='*45)
print(f'Você digitou o número {contagem[numero]}!')

# Solução com o "Continue"

while True:
    while True:
        numero = int(input('Digite um número entre 0 e 20: '))

        if 0 <= numero <= 20:
            break

        print('Tente novamente. ', end='')
    print('='*45)

    print(f'Você digitou o número {contagem[numero]}!')
    print('='*45)

    prossiga = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

    if prossiga == 'N':
        break

print('='*45)
print('PROGRAMA FINALIZADO!')

