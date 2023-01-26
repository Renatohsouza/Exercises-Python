cores = {  # cores normais

    'vermelho': '\033[31m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'branco': '\033[97m',
    'roxo': '\033[35m',
    'verde': '\033[32m',
    'ciano': '\033[36m',
    'limpa': '\033[m',


    # cores em negrito

    'vermelho em negrito': '\033[1;31m',
    'preto e branco': '\033[7;97;m',
    'azul em negrito': '\033[1;34m',
    'amarelo em negrito': '\033[1;33m',
    'branco em negrito': '\033[1;97m',
    'roxo em negrito': '\033[1;35m',
    'verde em negrito': '\033[1;32m',
    'ciano em negrito': '\033[1;36m',

    # cores sublinhadas

    'vermelho sublinhado': '\033[4;31m',
    'azul sublinhado': '\033[4;34m',
    'amarelo sublinhado': '\033[4;33m',
    'roxo sublinhado': '\033[4;35m',
    'branco sublinhado': '\033[4;97m',
    'verde sublinhado': '\033[4;32m',
    'ciano sublinhado': '\033[4;36m'
}
# TABELA DE CODIGOS #
#       STYLE
''' 
0   NONE (VAZIO)
1   BOLD (NEGRITO)
4   UNDERLINE (SUBLINHADO)
7   NEGATIVE (INVERSO)
'''
print(f'Limpo \033[m{0}\033[m')
print(f'Negrito \033[1;97m{1}\033[m')
print(f'Sublinhado \033[4;35m{4}\033[m')
print(f'Negativo \033[7;97m{7}\033[m')
