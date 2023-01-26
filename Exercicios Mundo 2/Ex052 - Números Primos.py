
numero = int(input('digite um numero: '))

cont = 0
for num in range (1, numero + 1):
    if numero % num == 0:
        print('\033[33m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print(f'{num}', end=' ')
print(f'\n\033[m O número {numero} foi divisivel {cont} vezes.')  

if cont == 2:
    print(' E por isso ele é um número PRIMO!')
else:
    print(' E por isso ele não é um número PRIMO!')
