salario = int(input('\33[32mQual o seu salario em R$: '))

if salario > 1250:
    salario = (10*salario)/100+salario
    print(f'\33[35mO seu salario agora é de \33[34mR${salario:.2f}\33[35m! ')
else:
    salario = (15*salario)/100+salario
    print(f'O valor do seu salario agora é de \33[36mR${salario:.2f}\33[35m! ')