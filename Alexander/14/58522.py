from string import digits, ascii_uppercase
from itertools import product

alph = digits + ascii_uppercase


for p in range(2, 37):

    for x, y in product(alph, repeat=2):
        try:
            if (
                int("32", p) * int("14", p) == int(x + y + "2", p)
            ):
                print(int(y + x, p))
        except:
            ...


