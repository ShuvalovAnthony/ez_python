from itertools import product


for a in range(78_000, 80_000):
    flag = True

    for x, y in product(range(1, 100_000), repeat=2):
        if not (
            (78125 != y + 4*x) or (a > x) and (a > y)
        ):
            flag = False
            break
      

    if flag:
        print("answ", a)
