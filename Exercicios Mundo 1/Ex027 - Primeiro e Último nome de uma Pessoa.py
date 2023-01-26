from time import sleep

print('---- Olá! Seja Bem Vindo! ----')
sleep(1)
nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print(f'Seu primeiro nome é: {n[0]}')
print(f'Seu ultimo nome é: {n[-1]}')
sleep(1)
print('>>>> INFORMAÇÃO ADICIONAL <<<<')
sleep(2)
print(f'Seu nome completo tem {len(nome) - nome.count(" ")} letras!')
