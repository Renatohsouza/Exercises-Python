print('---- Ola, Seja bem vindo Professor! ---')
from random import shuffle
al1 = input('Primeiro aluno: ')
al2 = input('Segundo aluno: ')
al3 = input('Terceiro aluno: ')
al4 = input('Qaurto aluno: ')
lista = [al1, al2, al3, al4]
sorteio = shuffle(lista)
print(f'A ordem de apresentação sera: {sorteio}')
print(lista)
print('Obrigado professor!')
