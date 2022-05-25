import os

def operandos():
    os.system('cls')
    op1 = float(input('Digite o valor para o operando 1.\n->'))
    op2 = float(input('Digite o valor para o operando 2.\n->'))
    return op1, op2

def soma(op1, op2):
    os.system('cls')
    print('Voce escolheu soma'.center(45, '='))
    resultado = op1 + op2
    print(f'O resultado da SOMA entre {op1} e {op2} foi {resultado}.')
    os.system('pause')

def subitracao(op1, op2):
    os.system('cls')
    print('Voce escolheu subtração'.center(45, '='))
    resultado = op1 - op2
    print(f'O resultado da SUBTRAÇÃO entre {op1} e {op2} foi {resultado}.')
    os.system('pause')

def multiplicacao(op1, op2):
    os.system('cls')
    print('Voce escolheu multiplicação'.center(45, '='))
    resultado = op1 * op2
    print(f'O resultado da MULTIPLICAÇÃO entre {op1} e {op2} foi {resultado}.')
    os.system('pause')

def divisão(op1, op2):
    os.system('cls')
    print('Voce escolheu divisão'.center(45, '='))
    resultado = op1 / op2
    print(f'O resultado da divisão entre {op1} e {op2} foi {resultado}.')
    os.system('pause')