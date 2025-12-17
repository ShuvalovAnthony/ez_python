# def f19(s, step=1): # 1p 2v 3p 4v 5p
#     # условие победы в задаче
#     if (
#         s <= 15 and step == 3
#     ):
#         return True
#     elif (
#         (s > 15 and step == 3) or
#         (s <= 15 and step < 3)
#     ):
#         return False
    

#     moves = [
#         f19(s - 3, step + 1),
#         f19(s - 8, step + 1),
#         f19(s//3, step + 1)
#     ]


#     if step%2 == 1: # ходы пети
#         return all(moves) # проигравший - любой ход all, неудачный ход - any
#     # ходы вани (четные)
#     return any(moves) # победитель - ВСЕГДА any


# for s in range(16, 299):
#     if f19(s):
#         print(s)
        

# def f20(s, step=1): # 1p 2v 3p 4v 5p
#     # условие победы в задаче
#     if (
#         s <= 15 and step == 4
#     ):
#         return True
#     elif (
#         (s > 15 and step == 4) or
#         (s <= 15 and step < 4)
#     ):
#         return False
    

#     moves = [
#         f20(s - 3, step + 1),
#         f20(s - 8, step + 1),
#         f20(s//3, step + 1)
#     ]


#     if step%2 == 1: # ходы пети
#         return any(moves) # проигравший - любой ход all, неудачный ход - any
#     # ходы вани (четные)
#     return all(moves) # победитель - ВСЕГДА any


# for s in range(16, 299):
#     if f20(s):
#         print(s)
        


def f21(s, step=1): # 1p 2v 3p 4v 5p
    # условие победы в задаче
    if (
        s <= 15 and step == 3
    ):
        return True
    elif (
        (s > 15 and step == 3) or
        (s <= 15 and step < 3)
    ):
        return False
    

    moves = [
        f21(s - 3, step + 1),
        f21(s - 8, step + 1),
        f21(s//3, step + 1)
    ]


    if step%2 == 1: # ходы пети
        return all(moves) # проигравший - любой ход all, неудачный ход - any
    # ходы вани (четные)
    return any(moves) # победитель - ВСЕГДА any


for s in range(16, 299):
    if f21(s):
        print(s)




54
55
59
60
61
153
154
155