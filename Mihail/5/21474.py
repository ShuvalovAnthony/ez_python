def num_to6(num):
    res = ''

    while num > 0:
        res += str(num % 6)
        num //= 6

    return res[::-1]

spisok = []

for num in range(1, 100000):
    num_6 = num_to6(num)
    summma = sum([int (i) for i in num_6])

    if summma % 5 == 0:
        num_6 = num_6.replace("0", "*")
        num_6 = num_6.replace("3", "0")
        num_6 = num_6.replace("*", "3")
        num_6 = "11" + num_6
    else:
        num_6 += "44"
        num_6 = num_6[0] + "05" + num_6[3:]

    r = int(num_6, 6)
    if r > 1500:
        spisok.append([r, num])

spisok = sorted(spisok, key=lambda x: (x[0], -x[1]))

for row in spisok[:10]:
    print(row)