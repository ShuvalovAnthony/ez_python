from itertools import product
from string import digits, ascii_uppercase


alph = digits + ascii_uppercase[:4]

counter = 0


def check(num: str):
    nechet_digits = []

    for digit in num:
        if digit in "13579BD": # alph[1::2]
            nechet_digits.append(digit)

    if len(nechet_digits) != 2:
        return False
    
    if nechet_digits[0] != nechet_digits[1]:
        return False
    
    for digit in "02468AC":
        if nechet_digits[0] + digit + nechet_digits[0] in num:
            return True
        
    return False


for num in product(alph, repeat=5):
    num = ''.join(num)

    if (
        num[0] != '0' and
        check(num)
    ):
        counter += 1

print(counter)
