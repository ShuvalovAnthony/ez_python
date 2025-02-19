from itertools import product


counter = 0


def check(num: str):
    if num[0] == "0": return False
    if len(set(num)) != len(num): return False

    for i in "246":
        num = num.replace(i, '0')
    for i in "357":
        num = num.replace(i, '1')
    
    if ("00" in num) or ("11" in num): return False

    return True


for num in product("0234567", repeat=5):
    num = ''.join(num)
    counter += check(num)

print(counter)
