from itertools import product
from string import digits, ascii_uppercase


alph = digits + ascii_uppercase[:6]


counter = 0


def check(num: str):
    for i in "2468ACE":
        num = num.replace(i, "0")
    for i in "3579BDF":
        num = num.replace(i, "1")

    return ("00" not in num) and ("11" not in num)


for num in product(alph, repeat=3):
    num = ''.join(num)

    if (
        # все цифры различны
        (len(num) == len(set(num))) and
        check(num) and
        num[0] != "0"
    ):
        counter += 1

print(counter)