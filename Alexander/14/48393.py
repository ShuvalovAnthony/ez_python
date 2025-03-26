from string import digits
from itertools import product


alph = digits[:8]

for x, y in product(alph, repeat=2):
    res = int(y + "04" + x + "5", 11) + int("253" + x + y, 8)

    if res%117 == 0:
        print(res//117)
        break
