nome = input('\33[31mDigite o seu nome completo.\n')

print('\n\33[32mSeu nome em caracteres maiúsculos é:')
print(nome.upper())

print('\n\33[33mSeu nome em caracteres minúsculos é:')
print(nome.lower())

print('\n\33[34mA quantidade total de letras no seu nome é:')
nome_junto = nome.replace(' ','')
print(len(nome_junto))

nome_separado = nome.split()
print('\n\33[35mA quantidade de letras no seu primeiro nome é de:')
print(len(nome_separado[0]))
