ps = str(input('Seja bem vindo(a), Digite seu nome: ')).strip().title()
print(f'Ola {ps}, Siga as instruções para descobrir a tabuada!')
n = int(input('Digite um numero: '))
n1 = n*1
n2 = n*2
n3 = n*3
n4 = n*4
n5 = n*5
n6 = n*6
n7 = n*7
n8 = n*8
n9 = n*9
n10 = n*10
# TESTE 1 - print(f'A tabuada do numero {n} é:\n{n1}\n{n2}\n{n3}\n{n4}\n{n5}\n{n6}\n{n7}\n{n8}\n{n9}\n{n10}\nObrigado por utilizar!')
# TESTE 2 - print(n, 'x 1 =', f'{n1}\n',n, f' X 2 = {n2}\n',n, f' X 3 = {n3}\n',n, f' X 4 = {n4}\n',n, f' X 5 = {n5}')
print('\033[1;35m-=\033[m'*7)
print(f'{n} x {1:2} = {n*1}')
print(f'{n} X {2:2} = {n*2}')
print(f'{n} X {3:2} = {n*3}')
print(f'{n} X {4:2} = {n*4}')
print(f'{n} X {5:2} = {n*5}')
print(f'{n} X {6:2} = {n*6}')
print(f'{n} X {7:2} = {n*7}')
print(f'{n} X {8:2} = {n*8}')
print(f'{n} X {9:2} = {n*9}')
print(f'{n} X {10} = {n*10}')
print('\033[1;35m-=\033[m'*7)
