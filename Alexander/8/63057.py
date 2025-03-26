from itertools import product


def check(num: str):
    for digit in set(num):
        if num.count(digit) > 3:
            return False
    
    for i in '468':
        num = num.replace(i, '2')
    for i in '357':
        num = num.replace(i, '1')

    return ('11' not in num) and ('22' not in num)
    


counter = 0

for num in product("12345678", repeat=9):
    num = ''.join(num)

    if check(num):
        counter += 1

print(counter)
    

