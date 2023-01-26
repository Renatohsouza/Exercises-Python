
soma = 0 #acumulador normalmente soma um valor
cont = 0 #contador normalmente conta +1
for numero in range (1, 501, 2):
    if numero % 3 == 0:
        soma += numero
        cont += 1
print(f'A soma entre todos {cont} valores solicitados é de {soma}')
     