# def f19(h1, h2, step=1): # 1p 2v 3p 4v 5p
#     # условие по камням + условие по шагу для 19ой конкретной задачи
#     if (h1*h2 >= 600) and (step == 3):
#         return True
#     elif (
#         ((h1*h2 >= 600) and (step < 3)) or
#         ((h1*h2 < 600) and (step == 3))
#     ):
#         return False


#     moves = [
#         f19(h1 - 3, h2 + 3, step + 1),
#         f19(h1 + 2, h2, step + 1)
#     ]

#     if step%2 == 0: # ходы вани - четные
#         return any(moves)
#     return all(moves)


# for s in range(1, 15):
#     if f19(40, s):
#         print(s)


# def f20(h1, h2, step=1): # 1p 2v 3p 4v 5p
#     # условие по камням + условие по шагу для 19ой конкретной задачи
#     if (h1*h2 >= 600) and (step == 4):
#         return True
#     elif (
#         ((h1*h2 >= 600) and (step < 4)) or
#         ((h1*h2 < 600) and (step == 4))
#     ):
#         return False


#     moves = [
#         f20(h1 - 3, h2 + 3, step + 1),
#         f20(h1 + 2, h2, step + 1)
#     ]

#     if step%2 == 0: # ходы вани - четные
#         return all(moves)
#     return any(moves)


# for s in range(1, 15):
#     if f20(40, s):
#         print(s)
        



def f21(h1, h2, step=1): # 1p 2v 3p 4v 5p
    # условие по камням + условие по шагу для 19ой конкретной задачи
    if (h1*h2 >= 600) and (step in (3, )):
        return True
    elif (
        ((h1*h2 >= 600) and (step < 3)) or
        ((h1*h2 < 600) and (step == 3))
    ):
        return False


    moves = [
        f21(h1 - 3, h2 + 3, step + 1),
        f21(h1 + 2, h2, step + 1)
    ]

    if step%2 == 0: # ходы вани - четные
        return any(moves)
    return all(moves)


for s in range(1, 15):
    if f21(40, s):
        print(s)


10
# 13

# 13