from string import digits, ascii_uppercase
from itertools import product


alph = digits + ascii_uppercase


for x, y, p in product(alph, alph, range(len(alph))):
    try:
        if (
            int(x + x + x + '8', p) + int('43' + x + '9', p) == \
            int(y + y + '04', p)
        ):
            print(int(y + y + x, p))
    except:
        ...
