from math import hypot

oposto = float(input('\33[32mQual o cumprimento do cateto oposto?\n'))
adjacente = float(input('Qual o cumprimento do cateto adjacente?\n\33[m'))

print(f'\33[32ma hipotenusa dos catetos informados é \33[31;1;42m{hypot(oposto, adjacente)}\33[m')