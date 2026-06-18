from itertools import product


counter = 0


for num in product("0123456", repeat=5):
    num = ''.join(num)

    if (
        (num[0] != '0') and
        (num.count("0") == 1) and
        (num.count("1") <= 2)
    ):
        counter += 1

print(counter)