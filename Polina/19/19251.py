# 19ая

def f(h, step=1): # 1p 2v 3p 4v 5p
    if (step == 3) and (h >= 132): return 1
    if (
        ((step == 3) and (h < 132)) or
        ((step < 3) and (h >= 132))
    ): return 0

    moves = [
        f(h + 3, step + 1),
        f(h + 6, step + 1),
        f(h*3, step + 1),
    ]

    if step%2 == 1:
        return all(moves)
    return any(moves)


for s in range(1, 132):
    if f(s):
        print(s)

# 20ая

def f(h, step=1): # 1p 2v 3p 4v 5p
    if (step == 4) and (h >= 132): return 1
    if (
        ((step == 4) and (h < 132)) or
        ((step < 4) and (h >= 132))
    ): return 0

    moves = [
        f(h + 3, step + 1),
        f(h + 6, step + 1),
        f(h*3, step + 1),
    ]

    if step%2 == 0:
        return all(moves)
    return any(moves)


for s in range(1, 132):
    if f(s):
        print(s)

# 21ая

def f(h, step=1): # 1p 2v 3p 4v 5p
    if (step in (3,)) and (h >= 132): return 1
    if (
        ((step == 3) and (h < 132)) or
        ((step < 3) and (h >= 132))
    ): return 0

    moves = [
        f(h + 3, step + 1),
        f(h + 6, step + 1),
        f(h*3, step + 1),
    ]

    if step%2 == 1:
        return all(moves)
    return any(moves)


res = []

for s in range(1, 132):
    if f(s):
        res.append(s)

print(res)