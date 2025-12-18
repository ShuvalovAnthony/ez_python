def f19(stone, step = 1): #p1 v2 p3 v4 p5
    if (stone <= 20) and (step == 3):
        return True

    elif (stone > 20 and step == 3) or (stone <= 20 and step < 3):
        return False

    moves = [
        f19(stone - 5, step + 1),
        f19(stone - 7, step + 1),
        f19(stone // 4, step + 1)
    ]

    if step % 2 == 0:
        return any(moves)
    return all(moves)

for s in range(21, 150):
    if f19(s):
        print(s)