from itertools import product


def check(num: str):
    if num[0] == '0': return False

    if len(set(num)) < 4: return False

    for i in '2468':
        num = num.replace(i, '0')
    for i in '3579':
        num = num.replace(i, '1')

    return ('00' not in num) and ('11' not in num)
    

counter = 0

for num in product("0123456789", repeat=4):
    num = ''.join(num)

    if check(num):
        counter += 1


print(counter)