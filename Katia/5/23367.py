from itertools import product
counter = 0 


def check(num: str):
    for i in "0123456": 
        if i*2 in num:
            return False

    return True

for num in product("0123456", repeat = 5):
    num = "".join(num)
    if (
        (num.count("6")==1)
        and (num[0]!="0")
        and check(num)
    ):
        counter += 1
print(counter)

