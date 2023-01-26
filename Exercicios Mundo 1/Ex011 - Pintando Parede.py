nome = input('digite seu nome: ')
print('Ola', nome, 'Seja bem vindo(a) a sua calculadora!')
altura = float(input('Digite a altura: '))
largura = float(input('Digite a Largura: '))
area = altura*largura
tinta = area/2
print(f'Sua parede mede {altura}X{largura} e sua area é de {area}m²!')
print(f'Para pintar sua parede, serão necessarios {tinta}L de tinta')
