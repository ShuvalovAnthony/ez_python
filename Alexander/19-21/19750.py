# def f(s, step=1): # 1p 2v 3p 4v 5p
#     if (step == 3) and (s <= 19): return True
#     if (
#         (step == 3 and s > 19) or
#         (step < 3 and s <= 19)
#     ): return False

#     moves = [
#         f(s - 5, step + 1)
#     ]

#     if s%2 == 0:
#         moves.append(f(s//2, step + 1))
#     if s%3 == 0:
#         moves.append(f(s//3, step + 1))
#     if (s%2 != 0) and (s%3 != 0):
#         moves.append(f(s + 1, step + 1))

#     if step%2:
#         return all(moves)
#     return any(moves)


# for s in range(20, 150):
#     if f(s):
#         print(s)



# def f(s, step=1): # 1p 2v 3p 4v 5p
#     if (step  == 2) and (s <= 19): return True
#     if (
#         (step == 2 and s > 19) or
#         (step < 2 and s <= 19)
#     ): return False

#     moves = [
#         f(s - 5, step + 1)
#     ]

#     if s%2 == 0:
#         moves.append(f(s//2, step + 1))
#     if s%3 == 0:
#         moves.append(f(s//3, step + 1))
#     if (s%2 != 0) and (s%3 != 0):
#         moves.append(f(s + 1, step + 1))

#     if step%2:
#         return any(moves)
#     return all(moves)


# for s in range(20, 60):
#     if f(s):
#         print(s)


# def f(s, step=1): # 1p 2v 3p 4v 5p
#     if (step == 3) and (s <= 19): return True
#     if (
#         (step == 3 and s > 19) or
#         (step < 3 and s <= 19)
#     ): return False

#     moves = [
#         f(s - 5, step + 1)
#     ]

#     if s%2 == 0:
#         moves.append(f(s//2, step + 1))
#     if s%3 == 0:
#         moves.append(f(s//3, step + 1))
#     if (s%2 != 0) and (s%3 != 0):
#         moves.append(f(s + 1, step + 1))

#     if step%2:
#         return all(moves)
#     return any(moves)


# for s in range(20, 70):
#     if f(s):
#         print(s)

