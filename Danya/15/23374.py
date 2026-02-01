from itertools import product

for a in range(1, 1000):
    flag = True

    for x, y in product(range(1, 1000), repeat=2):
        if not (
            (x < a) and
            (y < 3*a) or
            (2*x + y > 128)
        ):
            flag = False
            break

    if flag:
        print(a)
        break





# for a in range(1, 1000):
#     flag = True

#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if not (
#                 (x < a) and
#                 (y < 3*a) or
#                 (2*x + y > 128)
#             ):
#                 flag = False

#     if flag:
#         print(a)
