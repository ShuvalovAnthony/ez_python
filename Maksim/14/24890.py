from string import digits, ascii_uppercase

alph = digits + ascii_uppercase[:17]


def to_27(num: int):
    res = ''

    while num > 0: # while num:
        res += alph[num%27]
        num //= 27
    # остатки задом наперед пишем
    return res[::-1]

zeros = []

for x in range(1, 7290 + 1):
    num = 27**298 + 27**269 - x

    num_27 = to_27(num)

    zeros.append(num_27.count("0"))

print(max(zeros))
