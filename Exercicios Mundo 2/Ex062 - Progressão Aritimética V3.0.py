from time import sleep

print('>> Seja bem vindo! <<')
print('-='*12)

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

termo = primeiro
cont = 1
total = 0
opção = 10

while opção != 0:
    total += opção

    while cont <= total:
        print(f'{termo} - ', end='')
        cont +=1
        termo += razao
    print('PAUSA')
    opção = int(input('Quantos termos a mais você gostaria de mostrar? '))
print('-='*24)
print(f'Progressão finalizada com um {total} termos mostrados!')

