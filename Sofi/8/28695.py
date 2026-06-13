from itertools import product
from string import ascii_uppercase, digits

alph = digits + ascii_uppercase[:3]


counter = 0

def check(num: str):
    kolvo_nechet = 0
    for i in "13579B":
        kolvo_nechet += num.count(i)
    
    if kolvo_nechet != 3:
        return False

    for i in "13579B":
        if i*3 in num:
            return True
    return False

for num in product(alph, repeat=6):
    num = ''.join(num)

    if (
        num[0] != '0' and
        check(num)
    ):
        counter += 1

print(counter)

