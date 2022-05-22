cores = {'amarelo': '\33[33m',
         'vermelho': '\33[31m',
         'semcor': '\33[m',
         'azul': '\33[36m'}

print('-='*50)
nome=input(f"{cores['amarelo']}Qual o seu nome?")
print(f"Olá {cores['vermelho']}{nome}{cores['amarelo']} vamos fazer uma brincadeira com minhas habilidades, ainda limitadas, de programação. \n Leia as mensagens {cores['azul']}<True>{cores['amarelo']} como sendo verdadeiras e {cores['azul']}<False>{cores['amarelo']} como sendo falsas. ")
print(f"{cores['semcor']}-="*50)
entrada=input(f"{cores['amarelo']}digite algo.")

print(f"O tipo primitivo que vc digitou é{cores['azul']}", type(entrada))
print(f"{cores['amarelo']}O que você digitou foi um caractere alphanumerico?{cores['azul']}", entrada.isalnum())
print(f"{cores['amarelo']}O que você digitou está todo em maiúsculo?{cores['azul']}", entrada.isupper())
print(f"{cores['amarelo']}O que você digitou está todo em minúsculo?{cores['azul']}", entrada.islower())
