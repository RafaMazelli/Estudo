media = 0  # saber a media das idades
idadevelho = 0  # CONTROLE PRA SABER A IDADE DO MAIS VELHO
menos20 = 0  # CONTAGEM DE QUANTOS MENORES DE 20 ANOS
maisvelho = 0
print('-='*30)
for c in range(0, 4):  # PERGUNTANDO OS PARAMETROS
    nome = input(f'Digite o \33[33mnome\33[m da {c+1}ª pessoa: ') .strip() .upper()
    idade = int(input(f'Digite a \33[33midade\33[m da {c+1}ª pessoa: '))
    sexo = input(f'\33[33mSexo\33[m da {c+1}ª pessoa: [M/F] ') .strip() .upper()


    if c == 1:  # SOMANDO PARA TIRAR A MEDIA
        media = idade

    if sexo in 'Mm' and idade > idadevelho:  # SABENDO QUEM EH O MAIS VELHO
        idadevelho = idade
        maisvelho = nome

    if sexo in 'Ff' and idade < 20:  # CONTANDO MENORES DE 20 ANOS
        menos20 += 1

    media = media + idade  # SOMA PARA MEDIA DE IDADE
    print('-='*30)

media = media / 4  # TIRANDO A MEDIA

print(f'A media final das idades é {media:.1f}\nO mais velho do sexo masculino é {maisvelho.capitalize()}\n' f'A quantidade de menores de 20 anos do sexo feminino foi {menos20}')
