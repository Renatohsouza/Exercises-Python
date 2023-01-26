valor = float(input('Quanto você tem de dinheiro? R$ '))
dl = valor/5.30
eu = valor/5.25
print(f'Com \033[1;33mR${valor:.2f}\033[m você pode comprar \033[1;35mU${dl:.2f}\033[m ou \033[1;36mEUR{eu:.2f}\033[m!')
