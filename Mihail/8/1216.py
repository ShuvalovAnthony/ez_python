from itertools import product


counter = 0


for num in product("01234", repeat=6):
    num = ''.join(num)

    if (
        (num[-1] not in "34") and (num[0] != "1") and (num[0] != "0")
    ):
        counter += 1


print(counter)