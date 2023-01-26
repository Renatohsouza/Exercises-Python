from time   import sleep
print('Seja bem vindo ao Analisador de Triângulos!')
sleep(1)
print('-=' * 15)
a = float(input('Digite o valor do primeiro segmento:'))
b = float(input('Digite o valor do segundo segmento: '))
c = float(input('Digite o valor do terceiro segmento: '))
if a < b + c and b < a + c and c < a + b: #Errei apenas colando 'or' ao inves de "and' 2x.
    print('Os segmentos acima FORMAM um triângulo!')
else:
    print('Os segmentos acima NÃO FORMAM um triângulo!')
