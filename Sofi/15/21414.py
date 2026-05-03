from itertools import product

for a in range(500):
    flag = True

    for x in range(500):
        for y in range(500):
            if not (
                (5 < y) or (x > 32) or (x + 2*y < a)
            ):
                flag = False
                break

    if flag:
        print(a)
        # break
    



# for x, y in product(range(10), repeat=2):
#     print(x, y)
#     if y == 8:
#         break