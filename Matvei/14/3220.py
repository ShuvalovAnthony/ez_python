n = 3*16**2018 - 2*8**1028 - 3*4**1100 -2**1050 - 2022


counter = 0

while n > 0:
    if n%4 == 3:
        counter += 1

    n //= 4

print(counter)
    