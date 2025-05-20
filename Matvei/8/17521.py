from itertools import product


counter = 0

for num in product("01234567", repeat=5):
    num = ''.join(num)

    if (
        (num[0] != '0') and
        (num[0] not in '1357') and
        (num[-1] not in '26') and
        (num.count('7') <= 2)
    ):
        counter += 1

print(counter)