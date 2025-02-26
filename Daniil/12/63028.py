from itertools import product


def algo(s: str):
    while "00" not in s:
        s = s.replace("01", "220", 1)
        s = s.replace("02", "1013", 1)
        s = s.replace("03", "120", 1)
    return s


for ones, twos, tri in product(
    range(30, -1, -1), range(30, -1, -1), range(30, -1, -1)
    ):
    a = "0" + "1"*ones + "2"*twos + "3"*tri + "0"
    a = algo(a)

    if (a.count("1") == 13) and (a.count("2") == 18):
        print(ones + twos + tri + 2)
        break