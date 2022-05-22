frase = input('Digite uma frase: ') .strip() .upper() .replace(' ', '')
inverso = frase[::-1]
print(f'A frase digitada foi \33[33m{frase}\33[m e o inverso dela é \33[35m{inverso}\33[m')
if frase == inverso:
    print('\33[36mOpa, temos um palíndromo!')
else:
    print('\33[36mNão temos um palíndromo! :/')