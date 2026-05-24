from itertools import product

alph = "0123456789ABC"

counter = 0

def check(num: str):
    for digit in 'alph':
        if digit*2 in num:
            return False
        
    return True

for num in product(alph, repeat=5):
    num = ''.join(num)


    if (
        num[0] != '0' and
        num.count('0') == 1 and
        check(num)
    ):
        counter += 1

print(counter)