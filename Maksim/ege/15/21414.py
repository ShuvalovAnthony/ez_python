from itertools import product

for a in range(100):
    flag = True

    for x, y in product(range(100), repeat=2):
        if not (
            (5 < y) or (x > 32) or
            (x + 2*y < a)
        ):
            flag = False
            break
            
    if flag:
        print(a)
        break