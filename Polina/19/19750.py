# def f(h, step=1): # 1p 2v 3p 4v 5p
#     if (step == 3) and (h <= 19): return 1
#     if (
#         ((step == 3) and (h > 19)) or
#         ((step < 3) and (h <= 19))
#     ): return 0

#     moves = [
#         f(h - 5, step + 1)
#     ]

#     if h%2 == 0: moves.append(f(h//2, step + 1))
#     if h%3 == 0: moves.append(f(h//3, step + 1))
#     if (h%2 != 0) and (h%3 != 0): moves.append(f(h + 1, step + 1))

#     if step%2 == 1:
#         return all(moves)
#     return any(moves)



# for s in range(20, 300):
#     if f(s):
#         print(s)


# def f(h, step=1): # 1p 2v 3p 4v 5p
#     if (step == 4) and (h <= 19): return 1
#     if (
#         ((step == 4) and (h > 19)) or
#         ((step < 4) and (h <= 19))
#     ): return 0

#     moves = [
#         f(h - 5, step + 1)
#     ]

#     if h%2 == 0: moves.append(f(h//2, step + 1))
#     if h%3 == 0: moves.append(f(h//3, step + 1))
#     if (h%2 != 0) and (h%3 != 0): moves.append(f(h + 1, step + 1))

#     if step%2 == 0:
#         return all(moves)
#     return any(moves)



# for s in range(20, 100):
#     if f(s):
#         print(s)


# def f(h, step=1): # 1p 2v 3p 4v 5p
#     if (step in (3,)) and (h <= 19): return 1
#     if (
#         ((step == 3) and (h > 19)) or
#         ((step < 3) and (h <= 19))
#     ): return 0

#     moves = [
#         f(h - 5, step + 1)
#     ]

#     if h%2 == 0: moves.append(f(h//2, step + 1))
#     if h%3 == 0: moves.append(f(h//3, step + 1))
#     if (h%2 != 0) and (h%3 != 0): moves.append(f(h + 1, step + 1))

#     if step%2 == 1:
#         return all(moves)
#     return any(moves)


# res = []

# for s in range(20, 100):
#     if f(s):
#         res.append(s)

# print(res)
