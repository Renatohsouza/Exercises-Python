from time import sleep
print('--- Seja Bem Vindo! ---')
print('Neste programa iremos calcular o custo de uma viajem!')
sleep(1)
distancia = float(input('Qual a distância da viagem em KM? '))
pc = (distancia*0.50)
prc = (distancia*0.45)
if distancia <= 200:
    print(f'Preço até 200 km de distância R${pc:.2f}')
else:
    print(f'Preço para viajens mais longas R${prc:.2f}')
sleep(1)
print('-=-'*12)
print('>>> Obrigado e volte sempre!! <<<')

#### PRIMEIROS TESTES ####

# no if se eu fizer == 200 por exemplo, ele esta calculando apenas o 0,45 centavos para ambos.
## se eu colcoar <= 200 ele calcula apenas 0,50 para ambos.

### SOLUÇÂO ###

# No if, eu estava colando a variavel "pc" ao inves de 'DISTANCIA', ai ele calculava errado.
## Tambem posso, ao inves de criar uma variavel para cada calculo. criar a variavel preçõ dentro de if/else

#### EXEMPLO ####

# if distancia <= 200:
#   preço = distancia * 0.50
# else:
#   preço = distancia * 0.45
# print(f' O preço de sua passagem sera de R${preço:.2f}