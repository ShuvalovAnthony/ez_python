from itertools import product


def check(num: str):
    for i in set(num):
        if num.count(i) > 3: return False

    for i in "357": num = num.replace(i, "1")
    for i in "468": num = num.replace(i, "2")
    if ("11" in num) or ("22" in num): return False

    return True


counter = 0

for num in product("12345678", repeat=9):
    num = ''.join(num)
    counter += check(num)

print(counter)


