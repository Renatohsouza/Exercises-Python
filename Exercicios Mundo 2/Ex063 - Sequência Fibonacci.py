
print('-='*15)
print('>> Sequencia de Fibonacci << ')
print('-='*15)

numero = int(input('Quantos termos você quer mostrar? '))

t1 = 0
t2 = 1

print('~'*40)
print(f'{t1} - {t2}', end='')

cont = 3

while cont < numero:
    t3 = t1 + t2
    print(f' - {t3}', end='')
    t1 = t2
    t2 = t3
    cont +=1

print(' - FIM')
print('~'*40)
