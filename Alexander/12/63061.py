from itertools import product




for ed, dv, tr in product(range(50), repeat=3):
    a = '0' + '1'*ed + '2'*dv + '3'*tr + '0' # 15

    while '00' not in a:
        a = a.replace("01", "220", 1)
        a = a.replace("02", "1013", 1)
        a = a.replace("03", "120", 1) # 16

    if (a.count("1") == 13) and (a.count("2") == 18):
        print(ed + dv + tr + 2)
        break