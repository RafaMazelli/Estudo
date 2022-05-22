print('-='*40)
num1 = int(input('\33[33mDigite o primeiro numero.\n'))
num2 = int(input('Digite o segundo numero.\n\33[m'))
print('-='*40)

if num1 == num2:
    print('\33[36mOs dois numeros são iguais')
elif num1 > num2:
    print('\33[36mO primeiro numero é maior que o segundo!')
else:
    print('\33[36mO segundo numero é maior que o primeiro!')