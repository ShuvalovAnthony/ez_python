from math import ceil, floor


for n in range(1, 100):
    bit_na_pass = 5*n
    bait_na_pass = ceil(bit_na_pass/8)
    if bait_na_pass*7564230 > 32*1024**2:
        print(n)
        break