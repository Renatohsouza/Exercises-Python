# No exemplo abaixo eu utilizei a biblioteca math >> sqrt para calcular a raiz quadrada.
'''from math import sqrt
'co = float(input('Digite o valor do cateto oposto? '))
ca = float(input('Digite o valor do cateto adjacente: '))
s = (co*co)+(ca*ca)
h = (sqrt(s))
print(f'O valor da hipotenusa é: {h:.2f}')'''
# Ou h = (co *2 + ca *2 ) ** (1/2) --- que seria sem a bliblioteca sqrt

from math import  hypot
co = float(input('Digite o valor do cateto oposto: '))
ca= float(input('Digite o valor do cateto adjacente: '))
hi = hypot(co, ca)
print(f'O valor da hipotenusa é: {hi:.2f}')
