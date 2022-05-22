num = int(input('Digite um numero para ser convertido em uma das opções a seguir:'))

opcao = int(input('''(1) para BINARIO
(2) para OCTAL
(3) para HEXADECIMAL\n->'''))

if opcao == 1:
    print(f'O número digitado foi {num}, este número convertido é {bin(num)[2:]}')
elif opcao == 2:
    print(f'O número digitado foi {num}, este número convertido é {oct(num)[2:]}')
elif opcao == 3:
    print(f'O número digitado foi {num}, este número convertido é {hex(num)[2:]}')
else:
    print('Opção inválida!')