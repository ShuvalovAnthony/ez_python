from itertools import product


counter = 0


def check(num: str):
    for i in "246":
        num = num.replace(i, "0")
    
    for i in "357":
        num = num.replace(i, "1")

    return ("00" not in num) and ("11" not in num)


for num in product("01234567", repeat=6):
    num = ''.join(num)

    if (
        (num[0] != '0') and
        (len(set(num)) == len(num)) and
        check(num) and
        (int(num, 8)%5 == 0)
    ):
        counter += 1

print(counter)