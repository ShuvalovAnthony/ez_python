from itertools import product


def check(num: str):
    chet = []
    for digit in num:
        if digit in "02468A":
            chet.append(digit)

    return (
        (len(chet) == 2) and
        (len(set(chet)) == 1) and
        (chet[0]*2 in num)
    )


counter = 0

for num in product("0123456789AB", repeat=5):
    num = ''.join(num)

    if (
        (num[0] != '0') and
        check(num)
    ):
        counter += 1

print(counter)
