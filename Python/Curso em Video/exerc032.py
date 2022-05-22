ano = int(input('\33[32mDigite o ano que te direi se ele é ou nao bissexto.'))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\33[34mO ano é bissexto!')
else:
    print('\33[31mO ano não é bissexto!')