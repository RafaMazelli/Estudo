dias = int(input('\33[33mQuantos dias foi percorrido com o carro?\n'))
km = float(input('Quantos quilometros foram percorridos com o carro?\n\33[m'))
print('-='*50)

print(f'\33[33mO valor a ser pago pelo aluguel do carro é de \33[35mR${(dias*60)+(km*0.15):.2f}')