from itertools import product
from string import digits, ascii_uppercase


alph = digits + ascii_uppercase[:15]


def check(num: str):
    nechet_count = 0
    for nechet in alph[1::2]:
        nechet_count += num.count(nechet)

    ne_prev_5_cifr = 0
    for digit in "012345":
        ne_prev_5_cifr += num.count(digit)

    return (
        (nechet_count == 1) and
        (ne_prev_5_cifr <= 2)
    )


counter = 0

for num in product(alph, repeat=4):
    num = ''.join(num)

    if (
        (num[0] != '0') and
        check(num)
    ):
        counter += 1

print(counter)