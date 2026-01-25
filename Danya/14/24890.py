from string import digits, ascii_uppercase

def to_27(num: int):
    alph = digits + ascii_uppercase[:17]

    res = ''

    while num > 0:
        res += alph[num%27]
        num //= 27

    return res[::-1]


max_zeros = 0

for x in range(1, 7290 + 1):
    num = 27**298 + 27**269 - x
    num_27 = to_27(num)

    max_zeros = max(max_zeros, num_27.count("0"))

print(max_zeros)