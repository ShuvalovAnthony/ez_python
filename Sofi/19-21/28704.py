def f(s1, s2, step=1): # p1 v2 p3 v4 p5
    if (s1*s2 >= 516) and (step == 3):
        return True
    elif (
        ((s1*s2 < 516) and (step == 3)) or
        ((s1*s2 >= 516) and (step < 3))
    ):
        return False
    
    moves = [
        f(s1 + 3, s2, step + 1),
        f(s1, s2 + 3, step + 1),
        f(s1 + 13, s2, step + 1),
        f(s1, s2 + 13, step + 1)
    ]

    if step%2 == 1: #petya
        return any(moves)
    return any(moves)


for s2 in range(1, 74):
    if f(7, s2):
        print(s2)