nota1= int(input('\33[36mQual a nota da primeira unidade?'))
nota2= int(input('Qual a nota da segunda unidade?'))
media = (nota1 + nota2)/2
print('\33[m-='*40)

if media < 5:
    print('\33[33mVocê foi \33[31mREPROVADO!')
elif media >= 5 and media <= 6.9:
    print('\33[33mVocê foi para a \33[31mRECUPERAÇÃO')
else:
    print('\33[33mVocê foi \33[34mAPROVADO!')