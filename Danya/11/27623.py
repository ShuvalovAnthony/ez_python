from math import ceil, floor, log2

# ceil - потолок - округление вверх
# floor - пол - округление вниз


for l in range(1, 10_000):
    bit_per_symb = ceil(log2(10 + 26 + 8164))
    bytes_per_nomer = ceil(l*bit_per_symb/8)

    if 835*bytes_per_nomer > 156*1024:
        print(l)
        break