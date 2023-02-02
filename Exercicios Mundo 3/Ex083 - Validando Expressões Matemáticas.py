
'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e 
fechados na ordem correta.
'''

valor = str(input('Digite sua expressão: '))

contador = []

for simbolo in valor:
    if simbolo == '(':
        contador.append('(')
    elif simbolo == ')':
        if len(contador) > 0:
            contador.pop()
        else:
            contador.append(')')
            break

if len(contador) == 0:
    print('Sua expressão é Válida!')
else:
    print('Sua exressão está Errada!')
