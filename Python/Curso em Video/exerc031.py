dist = int(input('\33[34mQual a distancia em KM da sua viagem?'))
if dist <= 200:
    passagem=dist*0.50
    print(f'\33[32mO valor da sua passagem é de R${passagem:.2f}!')
else:
    passagem =dist*0.45
    print(f'\33[33mO valor da sua passagem é de R${passagem:.2f}!')