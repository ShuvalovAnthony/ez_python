from itertools import product


counter = 0


def check(num: str):
    for i in "357":
        num = num.replace(i, '1')
    
    return ('10' not in num) and ('01' not in num)


for num in product("012345678", repeat=5):
    num = ''.join(num)

    if (
        (num.count("0") == 1) and
        check(num) and
        (num[0] != '0')
    ):
        counter += 1

print(counter)