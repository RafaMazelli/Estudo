from datetime import datetime
ano = int(datetime.now().year)

nasc = int(input('\33[36mQual o seu ano de nascimento?'))

if (ano-nasc) < 18:
    certo = ((ano - nasc) - 18)*-1
    print(f'\33[35mVocê nao pode se alistar, ainda falta(m) \33[34m{certo}\33[35m ano(s).')
elif (ano-nasc) == 18:
    print('\33[33mParabens! Você ja pode fazer o alistamento!!')
else:
    errado = (ano - nasc) - 18
    print(f'\33[31mJa passou do tempo de você se alistar broder.. ja era pra vc ter se alistado a \33[32m{errado} \33[31mano(s)')
