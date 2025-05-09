# def f(s1, s2, step=1): # 1p 2v 3p 4v 5p
#     if ((s1 + s2 >= 81) and (step == 3)): return 1
#     if (
#         ((s1 + s2 < 81) and (step == 3)) or
#         ((s1 + s2 >= 81) and (step < 3))
#     ): return 0

#     moves = [
#         f(s1 + 1, s2, step + 1),
#         f(s1, s2 + 1, step + 1),
#         f(s1*2, s2, step + 1),
#         f(s1, s2*2, step + 1),
#     ]

#     if step%2 == 1: # нечетные
#         return any(moves)
#     return any(moves)


# for s2 in range(1, 74):
#     if f(7, s2):
#         print(s2)



# def f(s1, s2, step=1): # 1p 2v 3p 4v 5p
#     if ((s1 + s2 >= 81) and (step == 4)): return 1
#     if (
#         ((s1 + s2 < 81) and (step == 4)) or
#         ((s1 + s2 >= 81) and (step < 4))
#     ): return 0

#     moves = [
#         f(s1 + 1, s2, step + 1),
#         f(s1, s2 + 1, step + 1),
#         f(s1*2, s2, step + 1),
#         f(s1, s2*2, step + 1),
#     ]

#     if step%2 == 1: # нечетные
#         return any(moves)
#     return all(moves)


# for s2 in range(1, 74):
#     if f(7, s2):
#         print(s2)





def f(s1, s2, step=1): # 1p 2v 3p 4v 5p
    if ((s1 + s2 >= 81) and (step == 3)): return 1
    if (
        ((s1 + s2 < 81) and (step == 3)) or
        ((s1 + s2 >= 81) and (step < 3))
    ): return 0

    moves = [
        f(s1 + 1, s2, step + 1),
        f(s1, s2 + 1, step + 1),
        f(s1*2, s2, step + 1),
        f(s1, s2*2, step + 1),
    ]

    if step%2 == 1: # нечетные
        return all(moves)
    return any(moves)


for s2 in range(1, 74):
    if f(7, s2):
        print(s2)


'''
# Когда игрок может выиграть и на 1 и на 2ом ходу -
10 11 12 13 14 15 16 17

# Когда игрок может выиграть на первом ходу
10 12 13 14 16 17

# Из первого убираешь все, что есть во втором запуске 
11 15

'''