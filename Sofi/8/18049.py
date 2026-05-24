from itertools import product


alph = '012345678'

def check(num: str):
    for digit in alph:
        if digit*3 == num[-3:]:
            return False

    return True


counter = 0

for num in product(alph, repeat=7):
    num = ''.join(num)

    if (
        (num[0] not in '0246') and
        check(num) # len(set(num[-3:])) != 1
    ):
        counter += 1

print(counter)