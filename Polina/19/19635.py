# def f(h1, h2, step=1): # 1p 2v 3p 4v 5p
#     if (step == 3) and (h1 + h2 <= 100): return 1
#     if (
#         ((step == 3) and (h1 + h2 > 100)) or
#         ((step < 3) and (h1 + h2 <= 100))
#     ): return 0

#     moves = [
#         f(h1 - 3, h2 - 3, step + 1),
#         f(h1//2, h2, step + 1),
#         f(h1, h2//2, step + 1)
#     ]

#     return any(moves)


# for s in range(53, 150):
#     if f(48, s):
#         print(s)



# def f(h1, h2, step=1): # 1p 2v 3p 4v 5p
#     if (step == 2) and (h1 + h2 <= 100): return 1
#     if (
#         ((step == 2) and (h1 + h2 > 100)) or
#         ((step < 2) and (h1 + h2 <= 100))
#     ): return 0

#     moves = [
#         f(h1 - 3, h2 - 3, step + 1),
#         f(h1//2, h2, step + 1),
#         f(h1, h2//2, step + 1)
#     ]

#     if step%2 == 1:
#         return any(moves)
#     return all(moves)

# res1 = []
# res2 = []

# # [115, 116, 117, 118, 119, 120, 121, 122, 123, 115, 116, 117, 118, 119, 120, 121, 122, 123
# for s in range(53, 500):
#     if f(48, s):
#         res1.append(s)

# print(res1)

# # 115 229



# def f(h1, h2, step=1): # 1p 2v 3p 4v 5p
#     if (step in (3,)) and (h1 + h2 <= 100): return 1
#     if (
#         ((step == 3) and (h1 + h2 > 100)) or
#         ((step < 3) and (h1 + h2 <= 100))
#     ): return 0

#     moves = [
#         f(h1 - 3, h2 - 3, step + 1),
#         f(h1//2, h2, step + 1),
#         f(h1, h2//2, step + 1)
#     ]

#     if step%2 == 0:
#         return any(moves)
#     return all(moves)

# res = []
# for s in range(53, 500):
#     if f(48, s):
#         res.append(s)

# print(res)