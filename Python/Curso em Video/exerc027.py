n = input('\33[31mDigite seu nome: ').strip()
nome = n.split()

print(f'\33[33mSeu primeiro nome é: \33[36m{nome[0]}')
print(f'\33[33mSeu ultimo nome é: \33[36m{nome[len(nome)-1]}')



