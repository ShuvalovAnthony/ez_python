from string import digits, ascii_uppercase

alph = digits + ascii_uppercase[:17]

def to_27(num):
    res = ''

    while num > 0:
        res += alph[num%27]
        num //= 27

    return res[::-1]



for x in range(1, 27_001):
    exp = 3*27**9 + 2*27**6 + 27**3 - x

    exp_27 = to_27(exp)

    if exp_27.count("0") == 6:
        print(x)
        break