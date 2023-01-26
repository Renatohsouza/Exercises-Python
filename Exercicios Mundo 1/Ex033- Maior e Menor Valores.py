from time import sleep
print('Olã, Seja Bem vindo novamente!!')
print('-=-' * 15)
sleep(1)
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
menor = n1
if n2 < n1 and  n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'O  menor  valor digitado foi: {menor} ')
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O maior valor digitado foi: {maior}')
