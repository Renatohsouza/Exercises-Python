from time import  sleep
print('Olá! Seja bem vindo ao nosso testador de nomes!')
sleep(1)
nome = str(input('Digite seu nome completo: ')).strip()
print(f'Estamos verificando se você tem o sobrenome Silva...')
sleep(3)
print(f'{"SILVA" in nome.upper()}')
