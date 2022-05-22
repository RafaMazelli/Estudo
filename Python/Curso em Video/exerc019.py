import random
a1 = input('\33[33mdigite o nome do aluno.\n')
a2 = input('digite o nome do proximo aluno.\n')
a3 = input('Digite o nome do proximo aluno.\n')
a4 = input('Digite o nome do ultimo aluno.\n\33[m')
print('-='*50)

lista = [a1, a2, a3, a4]
aluno = random.choice(lista)

print(f'\33[33mO aluno escolhido foi o\33[35m {aluno}')