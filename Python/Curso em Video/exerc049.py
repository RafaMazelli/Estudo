print('-=' * 40)
print(' ' * 25, '\33[33mTABUADA(COM LAÇO FOR)\33[m')
print('-=' * 40)
num = int(input('\33[35mDigite um numero para ter a sua tabuada.\n\33[36m'))

for c in range(0,1000):
    print(f"{num} x {c} = {num * c}")
