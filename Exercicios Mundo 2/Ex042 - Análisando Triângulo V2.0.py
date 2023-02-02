from time import sleep

print('=== Verificando um Triângulo ===')
print('-='*15)
print("Preencha os campos abaixo para obter as informações!")
sleep(1)

ld1 = float(input('Digite o primeiro segmento: '))
ld2 = float(input('Digite o segundo segmento: '))
ld3 = float(input('Digite o terceiro segmento: '))

if ld1 < ld2 + ld3 and ld2 < ld1 + ld3 and ld3 < ld1 + ld2: #Condição aninhada
    print('Os segmentos formam um triangulo ', end='')
    if ld1 == ld2 == ld3:
        print('EQUILÁTERO!')
    elif ld1 != ld2 != ld3 != ld1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Não formam um triângulo!')
