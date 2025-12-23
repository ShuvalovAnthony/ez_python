from math import *
for x in range(1,  10**10):
    alf = ceil(log(10 + 60, 2))
    if ceil((x * alf) / 8) * 999 > 88 * 1024:
        print(x)
        break