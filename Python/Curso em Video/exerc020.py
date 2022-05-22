from random import shuffle
print('-='*40)
a1 = input('\33[32mQual o nome do aluno?\n')
a2 = input('Qual o nome do próximo aluno?\n')
a3 = input('Qual o nome do próximo aluno?\n')
a4 = input('Qual o nome do próximo aluno?\33[m\n')
print('-='*40)

lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'\33[32mA ordem é: \33[35m{lista}')