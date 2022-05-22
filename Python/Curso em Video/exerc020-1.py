from random import sample
print('-='*40)
a1 = input('\33[32mQual o nome do aluno?\n')
a2 = input('Qual o nome do próximo aluno?\n')
a3 = input('Qual o nome do próximo aluno?\n')
a4 = input('Qual o nome do próximo aluno?\33[m\n')
print('-='*40)

lista = [a1, a2, a3, a4]
ordem = sample(lista, k=2)
print(f'\33[32mA lista da ordem da apresentação é: \33[35m{ordem}')