from itertools import product


for a in range(90206 - 10, 90206 + 10):

    flag = True

    for x, y in product(range(90206, -1, -1), repeat=2):
        if not (
            (541241 != 5*x + y ) or (a > x) or (a > y)
        ):
            flag = False
            break


    if flag:
        print(a, '111')