from math import floor, ceil, log2

# alph_power - мощность алфавита (колво знаков в нем)
for alph_power in range(2, 1000): 
    i = ceil(log2(alph_power))

    bit_per_seriinik = i*105
    bait_per_seriinik = ceil(bit_per_seriinik/8)

    if bait_per_seriinik * 65536 >= 7*1024*1024:
        print(alph_power)
        break