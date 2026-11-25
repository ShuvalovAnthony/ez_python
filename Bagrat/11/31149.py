from math import log2, ceil, floor


for x in range(1, 100):
    i = ceil(log2(x)) # бит/символ
    seriinik_bit = i*440
    seriinik_byte = ceil(seriinik_bit/8)

    if seriinik_byte*1_892_412 >= 305_726*1024:
        print(x)
        break

    