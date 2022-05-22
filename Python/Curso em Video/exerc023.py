numero = int(input('\33[31mDigite um número entre 0 e 9999.\n'))


u = numero//1 % 10
d = numero//10 % 10
c = numero//100 % 10
m = numero//1000 % 10

print(f'\33[32mA unidade é:\33[35m {u}')
print(f'\33[32mA dezena é:\33[35m {d}')
print(f'\33[32mA centena é:\33[35m {c}')
print(f'\33[32mO milhão é: \33[35m{m}')