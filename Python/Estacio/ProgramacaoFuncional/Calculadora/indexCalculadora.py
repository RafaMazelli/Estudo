import os
import funcoes

respMenu = 0

#criar o menu
print('-=' * 30)
print('Calculadora teste'.center(60))
print('-=' * 30, '\n')

while respMenu != '5':
    respMenu = input('Digite uma das opções abaixo:\n1: Soma \n2: Subtração \n3: Multiplicação \n4: divisão\n5: Sair.\n->')
    
    if respMenu == '1':
        op1, op2 = funcoes.operandos()
        funcoes.soma(op1, op2)
        os.system('cls')
        
        
    elif respMenu == '2':
        op1, op2 = funcoes.operandos()
        funcoes.subitracao(op1,op2)
        os.system('cls')
       
    elif respMenu == '3':
        op1, op2 = funcoes.operandos()
        funcoes.multiplicacao(op1,op2)
        os.system('cls')

    elif respMenu == '4':
        op1, op2 = funcoes.operandos()
        while op2 == 0: 
            print('Não existe divisão por zero.. Escolha um valor para o operando 2 que não seja 0.')
            os.system('pause')
            op1, op2 = funcoes.operandos()
            os.system('cls')

        funcoes.divisão(op1,op2)
        os.system('cls')

    elif respMenu == '5':
        break
    
    else:
        print('Opção invalida!')
        os.system('pause')




#criar a tela de operações usando o cls do import os ver no ex

