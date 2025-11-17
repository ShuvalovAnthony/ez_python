# def f19(s, step=1): # 1p 2v 3p 4v 5p
#     # условие победы
#     if (s <= 30 and step == 3):
#         return True
#     if (
#         (s <= 30 and step < 3) or
#         (s > 30 and step == 3)
#     ):
#         return False
    
#     moves = [
#         f19(s - 3, step + 1),
#         f19(s - 5, step + 1),
#         f19(s//4, step + 1),
#     ]

#     # ПОБЕДИТЕЛЬ ВСЕГДА ХОДИТ any()
#     # Проигравший ходить all() если любой ход
#     # и any() если ход неудачный

#     if step%2 == 0: # четные ходы - Ваня
#         return any(moves)
#     return all(moves)



# for s in range(31, 500):
#     if f19(s):
#         print(s)
#         break

# def f20(s, step=1): # 1p 2v 3p 4v 5p
#     # условие победы
#     if (s <= 30 and step == 4):
#         return True
#     if (
#         (s <= 30 and step < 4) or
#         (s > 30 and step == 4)
#     ):
#         return False
    
#     moves = [
#         f20(s - 3, step + 1),
#         f20(s - 5, step + 1),
#         f20(s//4, step + 1),
#     ]

#     # ПОБЕДИТЕЛЬ ВСЕГДА ХОДИТ any()
#     # Проигравший ходить all() если любой ход
#     # и any() если ход неудачный

#     if step%2 == 0: # четные ходы - Ваня
#         return all(moves)
#     return any(moves)



# for s in range(31, 500):
#     if f20(s):
#         print(s)


def f21(s, step=1): # 1p 2v 3p 4v 5p
    # условие победы
    if (s <= 30 and (step == 3)): # (step == 3 or step == 5)
        return True
    if (
        (s <= 30 and step < 3) or
        (s > 30 and step == 3)
    ):
        return False
    
    moves = [
        f21(s - 3, step + 1),
        f21(s - 5, step + 1),
        f21(s//4, step + 1),
    ]

    # ПОБЕДИТЕЛЬ ВСЕГДА ХОДИТ any()
    # Проигравший ходить all() если любой ход
    # и any() если ход неудачный

    if step%2 == 0: # четные ходы - Ваня
        return any(moves)
    return all(moves)



for s in range(31, 500):
    if f21(s):
        print(s)

# Ваня выиграл первым или вторым ходом
124
125
126
132
133
134


# Ваня выиграл первым ходом
124
125
126