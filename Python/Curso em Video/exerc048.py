s = 0

for c in range(0,501):
    if (c % 2) != 0 and (c % 3) == 0:
         print(c)
         s = s + c
print(s)