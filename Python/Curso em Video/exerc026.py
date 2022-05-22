frase = input('\33[33mDigite uma frase qualquer.\n').upper()
qtde_a = frase.count('A')
posicao_frase = frase.find('A')

print(f'A sua frase tem \33[34m{qtde_a} \33[33mletras "A".')

print(f'A letra "A" começa no caractere \33[34m{posicao_frase+1}.')

print(f'\33[33mA ultima posição da letra "A" é \33[34m{frase.rfind("A")+1}')

