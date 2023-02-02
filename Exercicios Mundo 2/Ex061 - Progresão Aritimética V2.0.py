
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

termo = primeiro
cont = 1

while cont <= 10:
    print(f'{termo} - ', end='')
    cont +=1
    termo += razao
print('FIM!')

