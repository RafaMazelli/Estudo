from time import sleep
from random import randint
print('=-' * 40)
print(' ' * 25, '\33[36mPEDRA, PAPEL E TESOURA\33[m')
print('=-' * 40)
itens = ('Pedra', 'Papel', 'Tesoura')
player = int(input('Será que você consegue ganhar de mim neste jogo? Digite:\n(0)Para Pedra\n(1)Para Papel\n(2)Para tesoura\n'))
cpu = randint(0,2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
if (player - cpu) == 0:
    print(f"humm, empatou.. Eu e você jogamos {itens[player]}. Ná próxima, você não terá tanta sorte assim..")
elif (player == 0 and cpu == 1) or (player == 1 and cpu == 2) or (player == 2 and cpu == 0):
    print(f'Você jogou {itens[player]}?! Eu joguei {itens[cpu]}.. Ganheii, essa foi fácil!! hehehe')
elif (player == 0 and cpu == 2) or (player == 1 and cpu == 0) or (player == 2 and cpu == 1):
    print(f'Você jogou {itens[player]}?! Mas que cagada hein?! Eu joguei {itens[cpu]}, perdi! :(')
else:
    print('Opção inválida!!')