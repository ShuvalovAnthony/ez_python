# 19ая
def f(s, step=1): # 1p 2v 3p 4v 5p
    # условие победы в ЗАДАЧЕ
    if (step == 3) and (s >= 128): return True
    if (
        (step == 3 and s < 128) or
        (step < 3 and s >= 128)
    ): return False

    moves = [
        f(s + 2, step + 1),
        f(s + 5, step + 1),
        f(s*2, step + 1)
    ]

    if step%2 == 1:
        # ЛЮБОЙ ход Пети (проигравшего)
        # если бы был неудачный ход Пети - было бы any()
        return all(moves) 
    return any(moves) # победитель всегда any()



for s in range(2, 127):
    if f(s):
        print(s)


# 20ая
# def f(s, step=1): # 1p 2v 3p 4v 5p
#     # условие победы в ЗАДАЧЕ
#     if (step == 4) and (s >= 128): return True
#     if (
#         (step == 4 and s < 128) or
#         (step < 4 and s >= 128)
#     ): return False

#     moves = [
#         f(s + 2, step + 1),
#         f(s + 5, step + 1),
#         f(s*2, step + 1)
#     ]

#     if step%2 == 1:
#         return any(moves)
#     return all(moves)



# for s in range(2, 127):
#     if f(s):
#         print(s)


# 21ая
# def f(s, step=1): # 1p 2v 3p 4v 5p
#     # условие победы в ЗАДАЧЕ
#     if (step == 3) and (s >= 128): return True
#     if (
#         (step == 3 and s < 128) or
#         (step < 3 and s >= 128)
#     ): return False

#     moves = [
#         f(s + 2, step + 1),
#         f(s + 5, step + 1),
#         f(s*2, step + 1)
#     ]

#     if step%2 == 1:
#         return all(moves)
#     return any(moves)



# for s in range(2, 127):
#     if f(s):
#         print(s)


