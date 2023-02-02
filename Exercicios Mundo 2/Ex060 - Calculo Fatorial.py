'''numero = int(input('Digite um número para ver seu fatorial: '))

calculo = numero
fatorial = 1

print(f'Calculando {numero}! = ', end='')

while calculo > 0:
    print(f'{calculo}', end='')
    print(' X ' if calculo > 1 else ' = ', end='')
    fatorial *= calculo
    calculo -= 1
print(f'{fatorial}')'''

# Utilizando o for

numero = int(input('Digite um número para ver seu fatorial: '))

calculo = 0
fatorial = 1 # Multiplicando é 1 --- Somando ou subtraindo é 0 

for calculo in range (1,numero):
    fatorial *= numero
    numero -= 1
print(f'O fatorial é :{fatorial}')
