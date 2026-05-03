from string import digits, ascii_uppercase

alph = digits + ascii_uppercase[:17]

def to_27(num):
    res = ''

    while num > 0:
        res += alph[num%27]
        num //= 27

    return res[::-1]


res = []


for x in range(1, 7291):
    exp = 27**298 + 27**269 - x

    exp_27 = to_27(exp)

    res.append(exp_27.count("0"))

print(max(res))