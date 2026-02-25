from math import ceil, floor, log2


for i in range(1, 10000000):
    bit_per_px = ceil(log2(i))

    size = ceil(bit_per_px * 512 * 280 * 0.75) + 32*1024*8

    if size*64 <= 16*1024*1024*8:
        print(i)


