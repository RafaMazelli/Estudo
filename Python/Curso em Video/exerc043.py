preco = float(input('\33[33mQual o valor da compra?\n'))
pagamento = int(input('Digite \33[36m(1)\33[33m para á vista no dinheiro ou cheque;\nDigite \33[36m(2)\33[33m para a vista no cartão;\nDigite \33[36m(3)\33[33m para dividir no cartão em até 2x;\nDigite \33[36m(4)\33[33m para dividir no cartão em 3 ou mais vezes.\n '))

if pagamento == 1:
    preco = preco - (10 * preco)/100
    print(f'\33[34mO valor da sua compra é \33/35mR${preco:.2f}')
elif pagamento == 2:
    preco = preco - (5 * preco)/100
    print(f'\33[34mO valor da sua compra é \33[35mR${preco:.2f}')
elif pagamento == 3:
    print(f'\33[34mO valor da sua compra é \33[35mR${preco:.2f}')
elif pagamento == 4:
    preco = preco + (20 * preco)/100
    print(f'\33[34mO valor da sua compra é \33[35mR${preco:.2f}')