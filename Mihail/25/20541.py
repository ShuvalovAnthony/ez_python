from fnmatch import fnmatch


def check(num):
    num = str(num)
    res = 1

    for digit in num:
        res *= int(digit)

    return res


for num in range(4321, 10**9 + 1, 4321):
    mult = check(num)
    if fnmatch(str(num), "34*56?7") and (mult%10 == 0):
        print(num, mult)
