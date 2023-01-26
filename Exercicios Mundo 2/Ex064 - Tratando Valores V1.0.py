'''
 Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''
usuario = 0
contNum = -1
soma = 0

print(' >> Escreva um número inteiro e se quiser parar, digite 999! <<')
print('~'*65)
usuario = int(input('Digite um número inteiro: '))

while usuario != 999:
    usuario = int(input('Digite um número inteiro: ')) # O meu esta invertido a posição do Usuario dentro da condição While.
    contNum +=1 
    soma += usuario
    print('~'*30)

print(f'Você digitou {contNum} números!')
print(f'A soma de todos números digitados é de {soma}!')
print('~'*40)
print('>> FIM DO PROGRAMA! <<')

# Guanabara

'''
usuario = contNum = soma = 0 #<<<--- Aqui se todos acumuladores e contadores for 0, posso colocar tudo em uma linha.

usuario = int(input('Digite um número inteiro: ')) 

while usuario != 999:
    soma += usuario
    contNum += 1
    usuario = int(input('Digite um número inteiro: ')) # Aqui a ordem correta do Usuario estar, para o flag nao ser somado se o numero for 999.

print(f'Você digitou {contNum} números!')
print(f'A soma de todos números digitados é de {soma}!')
print('Fim do Programa!') '''
