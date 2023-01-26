nome = str(input('Digite o nome do aluno: ')).strip().title()
nt1 = float(input('Digite a primeira nota: '))
nt2 = float(input('Digite a segunda nota: '))
m = (nt1+nt2)/2
print(f'A média do Aluno {nome} é de: {m:.1f}!')
# Ou print('A media do aluno', (nome), f' é de: {(nt1+nt2)/2}!')
# Foi dividido por 2, pois sao apenas duas notas, se precisa-se de mais notas, seria acrescentado.
