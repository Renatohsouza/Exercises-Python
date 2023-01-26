
'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos. 
'''

print('~'*45)
print(f"{'- Cadastro de Pessoas -':^40}")
print('~'*45)

masculino = feminino = pessoas = 0

while True:
    idade = int(input('Qual a sua idade? '))
    print('~'*25)
    
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu genero? [M/F]: ')).upper().strip()[0]
    print('~'*25)

    print('USUÁRIO CADASTRADO!')
    print('~'*25)
    
    if idade >= 18:
        pessoas += 1
    if sexo == 'M':
        masculino += 1
    if sexo == 'F' and idade < 20:
        feminino =+ 1

    prossiga = ' '
    while prossiga not in 'SN':
        prossiga = str(input('Deseja continuar? [S/N]:  ')).upper().strip()[0]
        print('~'*25)

    if prossiga == 'N':
        break
    
print(f'Foram cadastrados {pessoas} pessoas maiores de 18 anos!')
print(f'Foram total de {masculino} Homens cadastrados!')
print(f'foi cadastrado um total de {feminino} Mulheres abaixo de 20 anos!')
print('~'*55)
print('>> Fim do programa! << ')
