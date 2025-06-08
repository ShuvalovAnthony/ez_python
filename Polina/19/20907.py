# def f(s1, s2, step=1): # p1 v2 p3 v4 p5
#     if (step == 3 and s1 + s2 >= 81): return True
#     elif (
#         (step == 3 and (s1 + s2 < 81)) or
#         (step < 3 and (s1 + s2 >= 81))
#     ): return False

#     moves = [
#         f(s1 + 1, s2, step + 1),
#         f(s1, s2 + 1, step + 1),
#         f(s1*2, s2, step + 1),
#         f(s1, s2*2, step + 1),
#     ]

#     if step%2 == 0:
#         return any(moves)
#     return any(moves)


# for s2 in range(1, 74):
#     if f(7, s2):
#         print(s2)
#         break



# def f(s1, s2, step=1): # p1 v2 p3 v4 p5
#     if (step == 4 and s1 + s2 >= 81): return True
#     elif (
#         (step == 4 and (s1 + s2 < 81)) or
#         (step < 4 and (s1 + s2 >= 81))
#     ): return False

#     moves = [
#         f(s1 + 1, s2, step + 1),
#         f(s1, s2 + 1, step + 1),
#         f(s1*2, s2, step + 1),
#         f(s1, s2*2, step + 1),
#     ]

#     if step%2 == 0:
#         return all(moves)
#     return any(moves)


# for s2 in range(1, 74):
#     if f(7, s2):
#         print(s2)


def f(s1, s2, step=1): # p1 v2 p3 v4 p5
    if (step == 3 and s1 + s2 >= 81): return True
    elif (
        (step == 3 and (s1 + s2 < 81)) or
        (step < 3 and (s1 + s2 >= 81))
    ): return False

    moves = [
        f(s1 + 1, s2, step + 1),
        f(s1, s2 + 1, step + 1),
        f(s1*2, s2, step + 1),
        f(s1, s2*2, step + 1),
    ]

    if step%2 == 0:
        return any(moves)
    return all(moves)


for s2 in range(1, 74):
    if f(7, s2):
        print(s2)


