print('--- Olá, Seja bem vindo!! ---')
num = int(input('Digite um numero: '))

#valor = str(num)
#print(f'A Unidade é: {valor[3]}')
#print(f'A Dezena é: {valor[2]}')
#print(f'A Centena é: {valor[1]}')
#print(f'O Milhar é: {valor[0]}')

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'A Unidade é: {u}')
print(f'A Dezena é: {d}')
print(f'A centena é: {c}')
print(f'O Milhar é: {m}')
