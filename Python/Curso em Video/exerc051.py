primeiro = int(input('\33[33mEscolha um primeiro termo para a progressão aritmetica: '))
razao = int(input('Escolha a razão para a progressao aritmetica: \33[36m'))
decimo = primeiro + (11 - 1) * razao

for c in range(primeiro, decimo , razao):
    print(c)
print('...')