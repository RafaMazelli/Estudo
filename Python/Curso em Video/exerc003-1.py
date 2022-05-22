cores = {'azul':'\33[36m',
         'semcor': '\33[m',
         'resposta': '\33[1;7;35m',
         'amarelo': '\33[0;33m'}

print('-='*70)
nome = input(f"{cores['amarelo']}Qual seu nome?\n-")
print(f"Olá {cores['azul']}{nome}{cores['semcor']}{cores['amarelo']}, escolha 2 numeros que te mostrarei os resultados de operações aritmeticas basicas entre eles!")
print(f"{cores['semcor']}-="*70)

n1 = int(input(f"{cores['azul']}Qual o primeiro número?\n"))
n2 = int(input(f"Qual o segundo numero?\n{cores['semcor']}"))
print(f"{cores['semcor']}-="*70)

print(f"{cores['amarelo']}As operações possíveis dos números {n1} e {n2} são: \n Soma:{cores['resposta']}{n1+n2}{cores['amarelo']}\n Subtração: {cores['resposta']}{n1-n2}{cores['amarelo']}\n Multiplicação: {cores['resposta']}{n1*n2}{cores['amarelo']}\n Divisão: {cores['resposta']}{n1/n2:.1f}{cores['amarelo']}\n Potencia: {cores['resposta']}{n1**n2}{cores['amarelo']}\n Divisão Inteira: {cores['resposta']}{n1//n2}{cores['amarelo']}\n Resto da Divisão: {cores['resposta']}{n1%n2}{cores['semcor']}")