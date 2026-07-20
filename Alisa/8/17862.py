from itertools import product


counter = 0


def check(num: str):
    count = 0
    for digit in "9AB":
        count += num.count(digit)

    return count <= 3


for num in product("0123456789AB", repeat=5):
    num = ''.join(num)

    if (
        (num.count("7") == 1) and
        check(num) and
        (num[0] != '0')
    ):

        counter += 1


print(counter)
