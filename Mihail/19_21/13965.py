# def f19(s1, s2, step=1): # p1 v2 p3 v4 p5
#     if (s1*s2 >= 541) and (step == 3):
#         return True
#     if (
#         ((s1*s2 < 541) and (step == 3)) or
#         ((s1*s2 >= 541) and (step < 3))
#     ):
#         return False

#     moves = [
#         f19(s1 + 10, s2, step + 1),
#         f19(s1, s2 + 10, step + 1),
#         f19(s1*2, s2, step + 1),
#         f19(s1, s2*2, step + 1),
#     ]

#     if step%2 == 0:
#         return any(moves)
#     return any(moves)


# for s2 in range(1, 91):
#     if f19(6, s2):
#         print(s2)
#         break


# def f20(s1, s2, step=1): # p1 v2 p3 v4 p5
#     if (s1*s2 >= 541) and (step == 4):
#         return True
#     if (
#         ((s1*s2 < 541) and (step == 4)) or
#         ((s1*s2 >= 541) and (step < 4))
#     ):
#         return False

#     moves = [
#         f20(s1 + 10, s2, step + 1),
#         f20(s1, s2 + 10, step + 1),
#         f20(s1*2, s2, step + 1),
#         f20(s1, s2*2, step + 1),
#     ]

#     if step%2 == 0:
#         return all(moves)
#     return any(moves)


# for s2 in range(1, 91):
#     if f20(6, s2):
#         print(s2)



def f21(s1, s2, step=1): # p1 v2 p3 v4 p5
    if (s1*s2 >= 541) and (step in (3, 5)):
        return True
    if (
        ((s1*s2 < 541) and (step == 5)) or
        ((s1*s2 >= 541) and (step < 5))
    ):
        return False

    moves = [
        f21(s1 + 10, s2, step + 1),
        f21(s1, s2 + 10, step + 1),
        f21(s1*2, s2, step + 1),
        f21(s1, s2*2, step + 1),
    ]

    if step%2 == 0:
        return any(moves)
    return all(moves)


for s2 in range(1, 91):
    if f21(6, s2):
        print(s2)
        break