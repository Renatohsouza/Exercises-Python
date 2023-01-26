print(f'{">> Indentificando um PALINDROMO <<":^40}')
print(' ')

frase = str(input('Digite sua frase: ')).strip().lower()

palavra = frase.split()
junto =''.join(palavra)
inverso =''
# inverso = junto[::-1] >>>> Esquema de fatiamento, ai não precisaria da utilização do for.

for palindromo in range (len(junto)-1,-1,-1):
    inverso += junto[palindromo]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print(' >> A palavra é um PALIDROMO!')
else:
    print(' >> A palavra NÃO é um PALINDROMO!')
print('FIM!')

