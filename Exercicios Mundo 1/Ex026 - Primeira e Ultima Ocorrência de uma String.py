from time import sleep

print('--- Olã, Seja Bem Vindo! ---')
sleep(1)
frase = str(input('Digite a frase de sua escolha: ')).strip().upper()

print(f'A letra A aparece: {frase.count("A")} vezes em seu nome!')
print(f'A letra A aparece pela 1° vez na posição {frase.find("A") + 1}')
print(f'E pela última vez na posição {frase.rfind("A") - frase.count(" ") - 1}')

# Utilizei o .count para eliminar os espaços entre as palavras e o -1 para ele me mostrar o valor exato
# da posição do ultimo A ( contando da Direita para esquerda)
