velocidade = int(input('\33[33mQual a velocidade do carro em km/h?\n'))

if velocidade >80:
    print('\33[31mVocê foi multado aí ó moral')
    multa = (velocidade-80)*7
    print(f'Voce vai pagar R${multa:.02f} de multa! x.x')
else:
    print('\33[34mTa tranquilo ta favorável! ;)')