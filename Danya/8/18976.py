from itertools import product
from string import digits, ascii_uppercase


alph = digits + ascii_uppercase[:10]


def check(num: str):
    for chet in alph[2::2]:
        num = num.replace(chet, "0")
    for nechet in alph[1::2]:
        num = num.replace(nechet, "1")

    return ('10101' == num) or ('01010' == num)

counter = 0

for num in product(alph, repeat=5):
    num = ''.join(num)

    if (
        (num[0] != '0') and
        (int(num[0], 20) + int(num[-1], 20) == 26) and
        check(num)
    ):
        counter += 1

print(counter)