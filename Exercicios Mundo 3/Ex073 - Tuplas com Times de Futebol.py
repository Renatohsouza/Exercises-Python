
'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.
'''

times = 'Palmeiras','Internacional','Fluminense','Corinthians','Flamengo','Atlético-PR','Atlético-MG','Fortaleza','São Paulo','Botafogo','América-MG','Santos','Goiás','Chapecoense','Coritiba','Cuiabá','Ceará','Atlético-GO','Avaí','Juventude'

print('~'*95)
print(f'Os 5 Primeiro times --> {times[:5]}')
print('~'*95)
print(f'Os 4 Últimos times --> {times[-4:]}')
print('~'*95)
print(f'Ordem Alfabética --> {sorted(times)}')
print('~'*95)
print(f"Posição time Chapecoense --> {times.index('Chapecoense')+1}º Lugar!")
print('~'*95)