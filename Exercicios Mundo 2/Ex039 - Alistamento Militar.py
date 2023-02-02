from datetime import date
from time import sleep

print(' == ALISTAMENTO BRASILEIRO ==')
sleep(1)

print('Você é so sexo Masculino ou Feminino?')
print('=-'*16)
genero = str(input('Digite sua opção: ')).strip().lower()

if genero == 'feminino':
    print('Mulheres no Brasil não são obrigadas a se alistar!!')
elif genero != 'feminino' and genero != 'masculino':
    print('Opção INVÁLIDA!!')
elif genero == 'masculino':
    print('Siga as instruções abaixo!')
    print('=-'*16)

    ano = int(input('Digite seu ano de nascimento: '))
    print('=-'*16)
    atual = date.today().year
    idade = atual - ano

    print(f'Quem nasceu em {ano} tem {idade} anos em 2022.')
    print('=-'*16)

    if idade == 18:
        print(f'Você deve se alistar imediatamente!!')
    elif idade < 18:
        print(f'Ainda faltam {18 - idade} ano(s) para seu alistamento')
        print(f'Você deve se alistar em {atual + (18 - idade)}!')
    elif idade > 18:    
        print(f'Você ja passou {idade - 18} ano(s) do tempo de se alistar!')
        print(f'Seu alistamento foi em {atual - (idade - 18)}!')
