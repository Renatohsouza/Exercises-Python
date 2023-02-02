# Minha resolução #

'''
sexo = ''
while sexo !='M' and sexo !='F':
    genero = str(input('Digite o sexo [M/F]: ')).strip().upper()[0] #Fatiando a string para pegar somente a 1º letra
    if genero =='M':
        print('Sexo Masculino Cadastrado com Sucesso!')
    elif genero =='F':
        print('Sexo Feminino cadastrado com Sucesso!')    
    else:
        print('Informação Inválida! Tente Novamente!')'''

# minha resoluçao + Guanabara #

'''
sexo =str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('Dados inválidos! Por Favor digite o sexo: ')).strip().upper()[0] # <<-- Fatiando a string para pegar somente a 1º letra
    if sexo =='M':
        print('Sexo Masculino Cadastrado com Sucesso!')
    elif sexo =='F':
        print('Sexo Feminino cadastrado com Sucesso!')   
print(f'Sexo {sexo} cadastrado com sucesso!')     <<< Aqui tem um porém, caso seja True a resposta inicial, haverá duplicidade de respostas, devido aos if's dentro do laço.  '''

# Resolução Guanabara (VALIDANDO DADOS) #

sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos! Por favor informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')

