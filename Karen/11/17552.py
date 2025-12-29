from math import floor, ceil, log2


# floor - пол - округлениеbit_na_simvol вниз
# ceil - потолок - округление вверх
# log2 - логарифм по основанию 2


for n in range(2, 50): # n - кол-во символов в алфавите (его мощность)
    bit_na_simvol = ceil(log2(n))

    bit_na_seriinik = bit_na_simvol*261

    bait_na_seriinik = ceil(bit_na_seriinik/8)

    if bait_na_seriinik*252500 > 31*1024*1024:
        print(n)


    # 1 1
    # 2 1
    # 3 2
    # 4 2
    # 5 3
    # 6 3
    # 7 3
    # 8 3

