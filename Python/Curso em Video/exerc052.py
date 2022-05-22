numero = int(input('Digite um numero para saber se ele é primo: '))
total = 0
for c in range (1,numero + 1):
    if numero % c == 0:
        print('\33[33m', end=' ')
        total = total + 1
    else:
        print('\33[31m', end=' ')
    print(f'{c}', end=' ')
if total == 2:
    print('\nO número é PRIMO!')
else:
    print('\nO numero NÃO É PRIMO!')