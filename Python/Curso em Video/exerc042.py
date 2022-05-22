peso = float(input('\33[33mQual o seu peso?\n'))
altura = float(input('Qual a sua altura em metros?\33[36m\n'))
imc = peso/(altura**2)

if imc < 18.5:
    print(f'\33[36mSeu IMC é \33[35m{imc:.1f}\33[36m. Você está abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print(f"Seu imc é \33[35m{imc:.2f}\33[36m. Você está com o peso ideal!")
elif imc >= 25 and imc < 30:
    print(f'Seu imc é \33[35m{imc:.1f}\33[36m. Você está com sobrepeso!')
elif imc >=30 and imc < 40:
    print(f'Seu imc é \33[35m{imc:.1f}\33[36m. Voce está obeso!')
else:
    print('Você está com obesidade mórbida!')