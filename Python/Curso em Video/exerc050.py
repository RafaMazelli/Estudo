s = 0
for c in range(0,6):
    num = int(input('\33[33mDigite um numero: \33[m'))
    if (num % 2) == 0:
        s += num
print(f'\33[35m{s}')