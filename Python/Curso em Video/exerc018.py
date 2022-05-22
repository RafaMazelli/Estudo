from math import cos, sin, tan
cores = {'amarelo': '\33[33m',
         'azul':'\33[36m',
         'semcor':'\33[m'}

angulo = float(input(f"{cores['amarelo']}Digite o angulo.\n{cores['semcor']}"))
print('-='*50)
print(f"{cores['amarelo']}o seno deste angulo é {cores['azul']}{sin(angulo):.2f}\n{cores['amarelo']}")
print(f"O cosseno deste angulo é {cores['azul']}{cos(angulo):.2f}\n{cores['amarelo']}")
print(f"A tangente deste angulo é {cores['azul']}{tan(angulo):.2f}\n{cores['semcor']}")