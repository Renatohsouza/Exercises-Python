
for numero in range(1, 51):
    if (numero % 2) == 0:
        print(numero)
print('Fim!')

""" OU

for numero in range(2, 51, 2): # Aqui economizamos "esforço" da máquina, evitando repetição de laços
    print(numero)              em excesso. Pulando de 2 em 2 casas, o pograma entrega o mesmo resultado.
print('FIM')

"""