maior = 0
menor = 0
for pess in range(1, 6):
    massa = float(input(f'Qual o peso da {pess}ª pessoa?'))
    if pess == 1:
        maior = massa
        menor = massa
    else:
        if massa > maior:
            maior = massa
        if massa < menor:
            menor = massa
print(f'O maior peso foi {maior} e o menor peso foi {menor}.')
