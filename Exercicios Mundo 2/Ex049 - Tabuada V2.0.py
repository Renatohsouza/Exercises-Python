
numero = int(input('Digite um número para ver sua tabuada: '))

for tabuada in range (1,11):
    resultado = numero * tabuada 
    print(f'{numero} X {tabuada} = {resultado}')
