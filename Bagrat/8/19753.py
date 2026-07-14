from itertools import product


def check(num: str):
    for i in "02468":
        num = num.replace(i, "_")

    return "__" not in num


counter = 0

for num in product("0123456789", repeat=6):
    num = ''.join(num)

    if (
        (num[0] != "0") and
        (int(num)%4 == 0) and
        (len(num) == len(set(num))) and
        check(num)
    ):
        counter += 1

print(counter)

