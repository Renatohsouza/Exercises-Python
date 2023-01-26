listra = '-='*15

print(listra)
print(f'{"10 TERMOS DE UMA PA":^30}')
print(listra)

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

decimo = termo + (10 - 1) * razao #cálculo matemático (Fórmula)

for pa in range (termo, decimo + razao, razao):
    print(f"{pa}",end=' - ')
print('Fim!')
