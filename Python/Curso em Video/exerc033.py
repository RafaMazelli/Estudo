n1 = int(input('\33[33mDigite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('\33[m@'*20)

print(f'\33[35mO numero menor foi \33[34m{menor}.')
print(f'\33[35mO numero maior foi \33[34m{maior}.')