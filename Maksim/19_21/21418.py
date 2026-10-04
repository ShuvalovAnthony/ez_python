# def f19(s, step=1): # 1p 2v 3p 4v 5p
#     if (s <= 87) and (step == 3):
#         return True
#     elif (
#         ((s <= 87) and (step < 3)) or
#         ((s > 87) and (step == 3))
#     ):
#         return False

#     moves = [
#         f19(s - 2, step + 1),
#         f19(s//2, step + 1)
#     ]

#     # ПОБЕДИТЕЛЬ ВСЕГДА any
#     # ПРОИГРАВШИЙ - all - если любой ход
#     # any - неудачный ход

#     if step%2 == 0:
#         return any(moves)
#     return all(moves)


# for s in range(89, 500):
#     if f19(s):
#         print(s)


# def f20(s, step=1): # 1p 2v 3p 4v 5p
#     if (s <= 87) and (step == 4):
#         return True
#     elif (
#         ((s <= 87) and (step < 4)) or
#         ((s > 87) and (step == 4))
#     ):
#         return False

#     moves = [
#         f20(s - 2, step + 1),
#         f20(s//2, step + 1)
#     ]

#     # ПОБЕДИТЕЛЬ ВСЕГДА any
#     # ПРОИГРАВШИЙ - all - если любой ход
#     # any - неудачный ход

#     if step%2 == 0:
#         return all(moves)
#     return any(moves)


# for s in range(89, 500):
#     if f20(s):
#         print(s)



def f21(s, step=1): # 1p 2v 3p 4v 5p
    if (s <= 87) and (step == 3):
        return True
    elif (
        ((s <= 87) and (step < 3)) or
        ((s > 87) and (step == 3))
    ):
        return False

    moves = [
        f21(s - 2, step + 1),
        f21(s//2, step + 1)
    ]

    # ПОБЕДИТЕЛЬ ВСЕГДА any
    # ПРОИГРАВШИЙ - all - если любой ход
    # any - неудачный ход

    if step%2 == 0:
        return any(moves)
    return all(moves)


for s in range(89, 500):
    if f21(s):
        print(s)


# 176
# 177
180
181
356
357



# 176
# 177