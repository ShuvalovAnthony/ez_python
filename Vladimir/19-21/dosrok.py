def f(h1, h2, step=1):
    if ((h1 + h2 >= 65) and (step == 3)):
        return True
    elif (
        ((h1 + h2 >= 65) and (step < 3)) or
        ((h1 + h2 < 65) and (step == 3))
    ):
        return False
    
    moves = [f(h1 + 1, h2, step + 1),
             f(h1 * 3, h2, step + 1),
             f(h1, h2 + 1, step + 1),
             f(h1, h2 * 3, step + 1)]
    
    return any(moves)


for h2 in range(1, 59):
    if f(6, h2):
        print(h2)