soma = 0
cont = 0
for numero in range (1,7):
    n = int(input(f'Digite {numero} numero: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'A soma dos {cont} números pares é de {soma}')