for ed in range(50):
    for dv in range(50):
        for tr in range(50):
            a = '0' + '1'*ed + '2'*dv + '3'*tr + '0'

            while '00' not in a:
                a = a.replace('01', '220', 1)
                a = a.replace('02', '1013', 1)
                a = a.replace('03', '120', 1)

            if a.count('1') == 13 and a.count('2') == 18:
                print(2 + ed + dv + tr)

            