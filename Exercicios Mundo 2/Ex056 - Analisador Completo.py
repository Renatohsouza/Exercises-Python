somaidade = 0
mediaidade = 0
maioridadehomem= 0
nomedomaisvelho = ''
totalmulher20 = 0

for pessoas in range (1,5):
    nome = str(input(f'Qual nome da {pessoas}º pessoa: ')).strip().capitalize()
    idade = int(input('Qual a idade? '))
    sexo = str(input('Qual o sexo? [M/F]: ')).strip().capitalize()

    somaidade += idade
    if pessoas == 1 and sexo == 'M':
        maioridadehomem = idade
        nomedomaisvelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomedomaisvelho = nome
    if sexo == 'F' and idade < 20:
        totalmulher20 +=1

mediaidade += somaidade / 4

print(f' A media de idade do grupo é: {mediaidade}')
print(f'O Homem mais velho se chama {nomedomaisvelho} e ele tem {maioridadehomem} anos.')
print(f'Existem {totalmulher20} mulher(es) abaixo dos 20 anos.')


'''  if pessoas == 1:
        conthomem += sexo
        contmulher += sexo
    else:
         if sexo > conthomem:
           conthomem += maiorrhomem

    if sexo == 'F' and 'F' <20:
        contmulher += sexo'''