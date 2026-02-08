from itertools import product
from string import digits, ascii_uppercase


alph = digits + ascii_uppercase[:6]

def check(num: str):
    for digit in alph:
        if digit*2 in num:
            return False
    return True

counter = 0

for num in product(alph, repeat=4):
    num = ''.join(num)

    if (
        (num.count("3") == 1) and
        check(num) and
        (num[0] != "0")
    ):
        counter += 1

print(counter)