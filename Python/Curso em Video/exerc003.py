cores = {'azul': '\33[36m',
         'semcor': '\33[0m',
         'lilas': '\33[7;1;35m'}

print('-='*30)
n1 = int(input(f"{cores['azul']} Qual o primeiro numero?{cores['semcor']}\n-"))
n2 = int(input(f"{cores['azul']} Qual o segundo numero?{cores['semcor']}\n-"))
print('-='*30)

print(f"A soma entre esses dois numeros é de {cores['lilas']} {n1+n2}!!{cores['semcor']}")