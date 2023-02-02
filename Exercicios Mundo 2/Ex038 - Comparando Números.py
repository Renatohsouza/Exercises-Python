from time import sleep

print('=== Seja bem vindo ! ===')
sleep(1)
print('*** Vamos comparar números! ***')
sleep(1)

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print('O primeiro número é maior!')
elif num1 < num2:
    print('O segundo número é maior!')
elif num1 == num2: # Ou utilizar o Else, ja que nao teria uma 4º opção.
    print('Os números são iguais!')
