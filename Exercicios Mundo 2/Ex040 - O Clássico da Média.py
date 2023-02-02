print(' === Calculando a Média de alunos === ')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print(f'Sua média é de {media:.1f}!')
    print('Você foi REPROVADO! :(')
elif media <= 6.9:
    print(f'Sua média foi de {media:.1f}!')
    print('Você esta de RECUPERAÇÃO!')
elif media >= 7.0:
    print(f'Sua média é de {media:.1f}')
    print('Você esta APROVADO!')
