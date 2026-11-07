def to_7(num):
    res = ''

    while num > 0:
        res += str(num%7)
        num //= 7

    return res[::-1]


for x in range(1, 2031): # x - int
    exp = 7**170 + 7**100 - x
    exp_7 = to_7(exp) # str

    if exp_7.count("0") == 70:
        print(x)