from random import randint
n = int(input('\33[34mEm qual numero estou pensando de 0 a 10?'))
num = randint(0,10)

if n==num:
    print('\33[33mAcertou mizeravi! Parabenoss!!')
else:
    print(f'\33[31mihhh perdeu aí oh moral, o numero era {num:.0f}')
print('\33[34mVolte depois pra mais uma.. vlew')


