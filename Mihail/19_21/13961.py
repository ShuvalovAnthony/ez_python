# def f19(s, step=1): # p1 v2 p3 v4 p5
#     # условие из задачи 
#     if (s >= 172) and (step == 3):
#         return True
#     if (
#         (s >= 172 and step < 3) or
#         (s < 172 and step == 3)
#     ):
#         return False
    
#     # все ходы из условия
#     moves = [
#         f19(s + 1, step + 1),
#         f19(s + 2, step + 1),
#         f19(s + 3, step + 1),
#         f19(s*2, step + 1),
#     ]


#     if step%2 == 0: # четные ходы - Ванины
#         return any(moves) # ПОБЕДИТЕЛЬ ВСЕГДА ХОДИТ any()
#     # для проигравшего - НЕУДАЧНЫЙ ход - any()
#     # ЛЮБОЙ ход - all()
#     return all(moves)


# for s in range(1, 172):
#     if f19(s):
#         print(s)


# def f20(s, step=1): # p1 v2 p3 v4 p5
#     # условие из задачи 
#     if (s >= 172) and (step == 4):
#         return True
#     if (
#         (s >= 172 and step < 4) or
#         (s < 172 and step == 4)
#     ):
#         return False
    
#     # все ходы из условия
#     moves = [
#         f20(s + 1, step + 1),
#         f20(s + 2, step + 1),
#         f20(s + 3, step + 1),
#         f20(s*2, step + 1),
#     ]


#     if step%2 == 0: # четные ходы - Ванины
#         return all(moves) # ПОБЕДИТЕЛЬ ВСЕГДА ХОДИТ any()
#     # для проигравшего - НЕУДАЧНЫЙ ход - any()
#     # ЛЮБОЙ ход - all()
#     return any(moves)


# for s in range(1, 172):
#     if f20(s):
#         print(s)

def f21(s, step=1): # p1 v2 p3 v4 p5
    # условие из задачи 
    if (s >= 172) and (step == 3):
        return True
    if (
        (s >= 172 and step < 3) or
        (s < 172 and step == 3)
    ):
        return False
    
    # все ходы из условия
    moves = [
        f21(s + 1, step + 1),
        f21(s + 2, step + 1),
        f21(s + 3, step + 1),
        f21(s*2, step + 1),
    ]


    if step%2 == 0: # четные ходы - Ванины
        return any(moves) # ПОБЕДИТЕЛЬ ВСЕГДА ХОДИТ any()
    # для проигравшего - НЕУДАЧНЫЙ ход - any()
    # ЛЮБОЙ ход - all()
    return all(moves)


# 1ый запуск - step in (3, 5)
# 2ой запуск это step == 3
for s in range(1, 172):
    if f21(s):
        print(s)

