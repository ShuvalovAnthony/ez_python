from itertools import product
from string import digits, ascii_uppercase


alph = digits + ascii_uppercase[:6] # 10 цифр + 6 буква = 16ти ричная
# print(alph) # ПРОВЕРЬ АЛФАВИТ


def check(num: str):
    for i in "02468ACE":
        if (i + "6" in num) or ('6' + i in num):
            return False
    return True


counter = 0

for num in product(alph, repeat=5):
    num = ''.join(num)

    if (
        (num.count("6") == 2) and
        check(num) and
        num[0] != "0"
    ):
        counter += 1

print(counter)
