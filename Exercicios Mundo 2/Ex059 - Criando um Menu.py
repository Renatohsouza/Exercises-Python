from time import sleep

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print('-='*16)

opção = 0

while opção != 5:
    print('''    [ 1 ] - Somar
    [ 2 ] - Multiplicar
    [ 3 ] - Maior Número
    [ 4 ] - Novos Números
    [ 5 ] - Sair do Programa''')
    print('-='*20)

    opção = int(input('Qual a sua opção: '))
    print('-='*16)

    if opção == 1:
        soma = n1 + n2
        print(f'A soma de {n1} + {n2} é de {soma}!')
    elif opção == 2:
        mult = n1 * n2
        print(f'A multiplicação de {n1} X {n2} é de {mult}!')
    elif opção == 3:
        if n1 > n2:
            print(f'O Maior valor é {n1}! E ele é o Primeiro número!')
        elif n2 > n1:
            print(f'O Maior valor é {n2}! E ele é o Segundo número!')
    elif opção == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        
    elif opção == 5:
        print('Finalizando o Programa...')
    else:
        print('X - Opção Inválida! - X')
    print('-='*16)
    sleep(2)
print('Fim do Programa!')

# Resolução simplificada Guanabara no item 3!
'''' ou
     if n1 > n2:
        maior = n1
     else:
         maior = n2
    print(f'Entre {n1} e {n2} o maior valor é {maior}!'''