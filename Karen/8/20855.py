from itertools import product
from string import digits, ascii_uppercase


alph = digits + ascii_uppercase[:3]


counter = 0
index = 0


def check(num: str):
    for i in '13579BD':
        num = num.replace(i, '_')

    return '__' not in num


for num in product(alph, repeat=3):
    num = ''.join(num)

    if num[0] == '0': continue

    if check(num) and (index%10 == 7):
        counter += 1

    index += 1


print(counter)