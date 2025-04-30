def f(s, step=1): # 1p 2v 3p 4v 5p
    # условие победы в задаче
    if (step == 3) and (s >= 67): return 1
    # условия поражения
    if (
        (step == 3 and s < 67) or
        (step < 3 and s >= 67)
    ): return 0

    # все возможные ходы
    moves = [
        f(s + 1, step + 1),
        f(s + 4, step + 1),
        f(s*3, step + 1)
    ]

    # победитель всегда ходит any()
    # проигравший ходит двумя вариантами
    # если проигравший ходит ЛЮБЫМ ходом - all()
    # если проигравший ходит НЕУДАЧНО это any()

    if step%2 == 1: # ходы Пети - нечетные
        return all(moves)
    return any(moves) # ходы Вани - четные


for s in range(1, 67):
    if f(s):
        print(s)



# def f(s, step=1): # 1p 2v 3p 4v 5p
#     # условие победы в задаче
#     if (step == 4) and (s >= 67): return 1
#     # условия поражения
#     if (
#         (step == 4 and s < 67) or
#         (step < 4 and s >= 67)
#     ): return 0

#     # все возможные ходы
#     moves = [
#         f(s + 1, step + 1),
#         f(s + 4, step + 1),
#         f(s*3, step + 1)
#     ]

#     # победитель всегда ходит any()
#     # проигравший ходит двумя вариантами
#     # если проигравший ходит ЛЮБЫМ ходом - all()
#     # если проигравший ходит НЕУДАЧНО это any()

#     if step%2 == 1: # ходы Пети - нечетные
#         return any(moves)
#     return all(moves) # ходы Вани - четные


# for s in range(1, 67):
#     if f(s):
#         print(s)



# def f(s, step=1): # 1p 2v 3p 4v 5p
#     # условие победы в задаче
#     if (step == 3) and (s >= 67): return 1
#     # условия поражения
#     if (
#         (step == 3 and s < 67) or
#         (step < 3 and s >= 67)
#     ): return 0

#     # все возможные ходы
#     moves = [
#         f(s + 1, step + 1),
#         f(s + 4, step + 1),
#         f(s*3, step + 1)
#     ]

#     # победитель всегда ходит any()
#     # проигравший ходит двумя вариантами
#     # если проигравший ходит ЛЮБЫМ ходом - all()
#     # если проигравший ходит НЕУДАЧНО это any()

#     if step%2 == 1: # ходы Пети - нечетные
#         return all(moves)
#     return any(moves) # ходы Вани - четные


# for s in range(1, 67):
#     if f(s):
#         print(s)




