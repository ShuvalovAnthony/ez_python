from math import ceil, floor, log2


alph = 10 + 26 + 34
i = ceil(log2(alph))


for l in range(1, 10_000): # l - длина номера серийного
    nomer_v_bit = i*l
    nomer_v_byte = ceil(nomer_v_bit/8)

    if nomer_v_byte*1142 > 305*1024:
        print(l)
        break