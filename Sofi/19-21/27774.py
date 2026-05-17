# def f(s1, s2, step=1): # p1 v2 p3 v4 p5
#     # условие победы
#     if (s1 + s2 >= 207) and (step == 3): # STEP В УСЛОВИЯХ ВСЕГДА +1
#         return True
#     elif (
#         ((s1 + s2 >= 207) and (step < 3)) or
#         ((s1 + s2 < 207) and (step == 3))
#     ):
#         return False
    
#     moves = [
#         f(s1 + 1, s2, step + 1),
#         f(s1, s2 + 1, step + 1),
#         f(s1*2, s2, step + 1),
#         f(s1, s2*2, step + 1),
#     ]

#     # победитель ВСЕГДА or / any
#     # проигравший - если любой ход - and / all, если неудачный - or / any
#     if step%2 == 0:
#         return any(moves)
#     return any(moves)


# for s2 in range(2, 190):
#     if f(17, s2):
#         print(s2)



def f(s1, s2, step=1): # p1 v2 p3 v4 p5
    # условие победы
    if (s1 + s2 >= 207) and (step == 4): # STEP В УСЛОВИЯХ ВСЕГДА +1
        return True
    elif (
        ((s1 + s2 >= 207) and (step < 4)) or
        ((s1 + s2 < 207) and (step == 4))
    ):
        return False
    
    moves = [
        f(s1 + 1, s2, step + 1),
        f(s1, s2 + 1, step + 1),
        f(s1*2, s2, step + 1),
        f(s1, s2*2, step + 1),
    ]

    # победитель ВСЕГДА or / any
    # проигравший - если любой ход - and / all, если неудачный - or / any
    if step%2 == 0: # vanya
        return all(moves)
    return any(moves) # petya


for s2 in range(2, 190):
    if f(17, s2):
        print(s2)