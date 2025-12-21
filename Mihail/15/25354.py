# from itertools import product


# def check(a, x, y):
#     return (a > max(x, y)) or (78125 != y + 4*x)


# for a in range(0, 100_000):
#     print(a)
#     flag = True

#     for x, y in product(range(1, 10**5), repeat=2):
#         if not check(a, x, y):
#             flag = False
#             break

#     if flag:
#         print(a, 'ANSW')
#         break


# from itertools import product


# a = 78122

# flag = True

# for x, y in product(range(10**5), repeat=2):
#     if not (
#         (a > x) and (a > y) or (78125 != y + 4*x)
#     ):
#         flag = False
#         print(a, x, y, 'false')
#         break

