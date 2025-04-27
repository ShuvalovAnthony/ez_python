from itertools import combinations


def d(x):
    return 15 <= x <= 40


def c(x):
    return 21 <= x <= 63


# def a(x, e):
#     return 7 <= x <= e

def a(x):
    return 7 <= x <= 20


# for e in range(8, 100):
#     flag = True


#     for x in range(0, 100):
#         if not (
#             d(x) <= 
#             (
#                 (
#                     (not c(x)) and (not a(x, e))
#                 ) <=
#                 (
#                     not d(x)
#                 )
#             )
#         ):
#             flag = False
#             break

#     if flag:
#         print(e)
#         break


flag = True


for x in range(0, 100):
    if not (
        d(x) <=
        (
            ((not c(x))and (not a(x))) <=
            (not d(x))
        )
    ):
        flag = False
        break

if flag:
    print("YES")
