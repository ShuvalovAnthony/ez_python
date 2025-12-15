# def f19(s, step=1): # p1 v2 p3 v4 p5
#     if (
#         s >= 125 and step == 3
#     ):
#         return True
#     elif (
#         (s < 125 and step == 3) or
#         (s >= 125 and step < 3)
#     ):
#         return False
    
#     moves = [
#         f19(s + 2, step + 1),
#         f19(s + 4, step + 1),
#         f19(s*2, step + 1)
#     ]

#     if step%2 == 0:
#         return any(moves) # победитель ВСЕГДА any
#     return all(moves)


# for s in range(1, 125):
#     if f19(s):
#         print(s)

# def f20(s, step=1): # p1 v2 p3 v4 p5
#     if (
#         s >= 125 and step == 4
#     ):
#         return True
#     elif (
#         (s < 125 and step == 4) or
#         (s >= 125 and step < 4)
#     ):
#         return False
    
#     moves = [
#         f20(s + 2, step + 1),
#         f20(s + 4, step + 1),
#         f20(s*2, step + 1)
#     ]

#     if step%2 == 0:
#         return all(moves) # победитель ВСЕГДА any
#     return any(moves)


# for s in range(1, 125):
#     if f20(s):
#         print(s)


def f21(s, step=1): # p1 v2 p3 v4 p5
    if (
        s >= 125 and step == 3
    ):
        return True
    elif (
        (s < 125 and step == 3) or
        (s >= 125 and step < 3)
    ):
        return False
    
    moves = [
        f21(s + 2, step + 1),
        f21(s + 4, step + 1),
        f21(s*2, step + 1)
    ]

    if step%2 == 0:
        return any(moves) # победитель ВСЕГДА any
    return all(moves)


for s in range(1, 125):
    if f21(s):
        print(s)


55
56
# 61
# 62

# 61
# 62