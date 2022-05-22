cores = {'amarelo': '\33[33m',
         'azul': '\33[34m',
         'vermelho': '\33[31m',
         'semcor':'\33[m',
         'roxo': '\33[35m'}

r1 = int(input(f"{cores['amarelo']}Qual o primeiro seguimento?"))
r2 = int(input('qual o segundo seguimento?'))
r3 = int(input(f"Qual o terceiro seguimento?{cores['semcor']}"))
print('-='*50)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f"{cores['roxo']}Esses seguimentos {cores['azul']}PODEM FORMAR {cores['roxo']}um triangulo!")
else:
    print(f"{cores['roxo']}Esses seguimentos {cores['vermelho']}NAO PODEM {cores['roxo']}formar um triangulo!")