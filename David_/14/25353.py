def to_27(num: int):
    from string import digits, ascii_uppercase

    alph = digits + ascii_uppercase

    res = ''

    while num > 0:
        res += alph[num%27]
        num //= 27

    return res[::-1]



for x in range(1, 27001):
    num = 3*27**9 + 2*27**6 + 27**3 - x
    num_27 = to_27(num)

    if num_27.count("0") == 6:
        print(x)
        break
