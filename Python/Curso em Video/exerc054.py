from datetime import date

anoatual = date.today().year
maioridade = 0
menoridade = 0

for c in range(0, 7, 1):
    ano = int(input(f'Em qual ano a {c+1}ª pessoa nasceu?'))
    if anoatual - ano >= 21:
        maioridade += 1
    else:
        menoridade += 1
print(f'\33[33m{maioridade}\33[m pessoas \33[35mja atingiram\33[m a maioridade e \33[33m{menoridade}\33[m '
      f'ainda \33[35mnão\33[m atingiram.')
