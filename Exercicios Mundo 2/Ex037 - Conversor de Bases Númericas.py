
numero = int(input('Digite um numero inteiro: '))

print('''Escolha uma das bases para a conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')

opção = int(input('Sua opção: '))

if opção == 1:
    print(f'{numero} convertido para BINÁRIO é igual a {bin(numero)[2:]}')
elif opção == 2:
    print(f'{numero} convertido para OCTAL é igual a {oct(numero)[2:]}')
elif opção == 3:
    print(f' {numero} convertido para HEXADECIMAL é igual a {hex(numero)[2:]}')
else:
    print('Opção inválida!')
