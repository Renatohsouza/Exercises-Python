
maiorpeso = 0
menorpeso = 0

for pessoa in range (1,6):
    peso = float(input(f'Qual o peso da {pessoa}º pessoa? '))

    if pessoa == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso

print(f'O maior peso foi de: {maiorpeso} Kg. ')
print(f'O menor peso foi de {menorpeso} Kg.')