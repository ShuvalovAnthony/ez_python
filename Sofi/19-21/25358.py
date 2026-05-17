# def f(s, step=1): # p1 v2 p3 v4 p5
#     if (s >= 125) and (step == 3):
#         return True
#     elif (
#         ((s < 125) and (step == 3)) or
#         ((s >= 125) and (step < 3))
#     ):
#         return False
    
#     moves = [
#         f(s + 2, step + 1),
#         f(s + 4, step + 1),
#         f(s*2, step + 1),
#     ]

#     if step%2 == 0: # V
#         return any(moves)
#     else: # Petya
#         return all(moves)


# for s in range(1, 125):
#     if f(s):
#         print(s)
#         break


# def f(s, step=1): # p1 v2 p3 v4 p5
#     if (s >= 125) and (step == 4):
#         return True
#     elif (
#         ((s < 125) and (step == 4)) or
#         ((s >= 125) and (step < 4))
#     ):
#         return False
    
#     moves = [
#         f(s + 2, step + 1),
#         f(s + 4, step + 1),
#         f(s*2, step + 1),
#     ]

#     if step%2 == 0: # Vanya
#         return all(moves)
#     else: # Petya
#         return any(moves)


# for s in range(1, 125):
#     if f(s):
#         print(s)


# def f(s, step=1): # p1 v2 p3 v4 p5
#     if (s >= 125) and (step == 3):
#         return True
#     elif (
#         ((s < 125) and (step == 3)) or
#         ((s >= 125) and (step < 3))
#     ):
#         return False
    
#     moves = [
#         f(s + 2, step + 1),
#         f(s + 4, step + 1),
#         f(s*2, step + 1),
#     ]

#     if step%2 == 0: # Vanya
#         return any(moves)
#     else: # Petya
#         return all(moves)


# for s in range(1, 125):
#     if f(s):
#         print(s)

# 2 запуска 
'''
первый запуск - выигрыш первым или вторым ходом
if (s >= 125) and (step == 3 or step == 5): # ‼️
        return True
    elif (
        ((s < 125) and (step == 5)) or # ‼️
        ((s >= 125) and (step < 5)) # ‼️
    ):
        return False

55
56
61
62


второй запуск - выигрыш ТОЛЬКО первым
if (s >= 125) and (step == 3): # ‼️
        return True
    elif (
        ((s < 125) and (step == 3)) or # ‼️
        ((s >= 125) and (step < 3)) # ‼️
    ):
        return False

61
62


из первого результата удаляем все, что есть во втором
55
56
'''