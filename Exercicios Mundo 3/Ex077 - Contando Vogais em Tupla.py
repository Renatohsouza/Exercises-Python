
'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

palavras = 'casa','carro','andaime','pipoca','lapis','cortina','bicicleta','treino'

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

'''
Para cada palavra dentro de palavra ele imprime o print
    Cada item é uma lista, entao eu posso analizar a letra dentro da palavra.
        se a palavra conter as letras 'aeiou', ele ira imprimir as vogais.
'''