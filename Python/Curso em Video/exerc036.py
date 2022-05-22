casa = float(input('\33[33mQual o valor da casa?\n'))
salario = float(input('Qual o seu salario?\n'))
tempo = int(input('Em quantos anos pretende pagar?\n\33[m'))
tempo = tempo*12
print('-='*30)

if casa / tempo <= (30*salario)/100 :
    print('\33[36mCredito aprovado!!\33[m')
else:
    print('\33[31mCredito negado')