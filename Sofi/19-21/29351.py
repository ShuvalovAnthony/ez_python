# def f(s1, s2, step=1): # p1 v2 p3 v4 p5
#     if (s1 + s2 >= 154) and (step == 3):
#         return True
#     elif (
#         ((s1 + s2 < 154) and (step == 3)) or
#         ((s1 + s2 >= 154) and (step < 3))
#     ):
#         return False
    
#     moves = [
#         f(s1 + 4, s2, step + 1),
#         f(s1, s2 + 4, step + 1),
#         f(s1*3, s2, step + 1),
#         f(s1, s2*3, step + 1),
#     ]

#     if step%2 == 1:
#         return any(moves)
#     return any(moves)


# for s2 in range(1, 143):
#     if f(11, s2):
#         print(s2)
#         break


# def f(s1, s2, step=1): # p1 v2 p3 v4 p5
#     if (s1 + s2 >= 154) and (step == 4):
#         return True
#     elif (
#         ((s1 + s2 < 154) and (step == 4)) or
#         ((s1 + s2 >= 154) and (step < 4))
#     ):
#         return False
    
#     moves = [
#         f(s1 + 4, s2, step + 1),
#         f(s1, s2 + 4, step + 1),
#         f(s1*3, s2, step + 1),
#         f(s1, s2*3, step + 1),
#     ]

#     if step%2 == 1:
#         return any(moves)
#     return all(moves)


# for s2 in range(1, 143):
#     if f(11, s2):
#         print(s2)



def f(s1, s2, step=1): # p1 v2 p3 v4 p5
    if (s1 + s2 >= 154) and (step == 3):
        return True
    elif (
        ((s1 + s2 < 154) and (step == 3)) or
        ((s1 + s2 >= 154) and (step < 3))
    ):
        return False
    
    moves = [
        f(s1 + 4, s2, step + 1),
        f(s1, s2 + 4, step + 1),
        f(s1*3, s2, step + 1),
        f(s1, s2*3, step + 1),
    ]

    if step%2 == 1:
        return all(moves)
    return any(moves)


for s2 in range(1, 143):
    if f(11, s2):
        print(s2)


41
42
44
# 47

# 47