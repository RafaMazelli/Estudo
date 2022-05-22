from time import sleep

print('\33[33mNúmeros pares de 1 a 50\33[36m')
sleep(1), print('.'), sleep(1)
for c in range(1,51):
    if (c % 2) == 0:
        print(c)
        sleep(0.3)