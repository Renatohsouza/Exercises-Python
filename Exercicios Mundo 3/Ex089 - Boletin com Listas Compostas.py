
'''
 Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
 No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''
alunos = []

while True:
    nome = str(input('Nome do Aluno: ')).capitalize()
    nt1 = float(input('Primeira nota: '))
    nt2 = float(input('Segunda nota: '))
    media = (nt1 + nt2) / 2
    alunos.append([nome, [nt1, nt2], media])
    
    escolha = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if escolha == 'N':
        break

print('='*30)
print(f'{"Nº":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*30)
for i, a in enumerate(alunos):
    print(f'{1:<4}{a[0]:<10}{a[2]:>8.1f}')
    
while True:
    print('='*30)
    pergunta = int(input('Mostrar notas de qual aluno? [999 finaliza]: '))

    if pergunta == 999:
        print('Programa finalizado!')
        break
    if pergunta <= len(alunos) - 1:
        print(f'Notas de {alunos[pergunta][0]} são {alunos[pergunta][1]}')
print('>> VOLTE SEMPRE <<')
