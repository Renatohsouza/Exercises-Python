
'''
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

continuar ='S'
media = soma = count =0
maiorValor = menorValor = 0

while continuar != 'N':
    num = int(input('Digite um número inteiro: '))
    print('~'*45)
    soma += num
    count += 1
    continuar = str(input('Deseja continuar a digitar valores? [S/N] ')).upper().strip()
    print('~'*45)

    if count == 1:      # <<<--- Aqui não estava dando certo pois eu estava declarando a variavel num, ao inves de count.
        maiorValor = num
        menorValor = num
    else:
        if num > maiorValor:
            maiorValor = num
        if num < menorValor:
            menorValor = num

media = soma / count    # <<<--- A média nao estava correta, pois eu nao havia mencionado um contador de somar as vezes que o usuario digitou.

print(f'Você digitou {count} números e a média foi de {media:.2f}!')
print(f'O maior valor digitado foi: {maiorValor}!') 
print(f'o Menor valor digitado foi: {menorValor}!')
print('~'*45)
print('>> Fim do Programa! <<')
