def f20(s, step=1): # p1 v2 p3 v4 p5
    # условие из задачи 
    if (s >= 39) and (step == 4):
        return True
    if (
        (s >= 39 and step < 4) or
        (s < 39 and step == 4)
    ):
        return False
    
    # все ходы из условия
    moves = [
        f20(s + 1, step + 1),
        f20(s + 3, step + 1),
        f20(s*2, step + 1),
    ]


    if step%2 == 0: # четные ходы - Ванины
        return all(moves) # ПОБЕДИТЕЛЬ ВСЕГДА ХОДИТ any()
    # для проигравшего - НЕУДАЧНЫЙ ход - any()
    # ЛЮБОЙ ход - all()
    return any(moves)


for s in range(1, 39):
    if f20(s):
        print(s)

print('-'*30)

def f20(s, step = 1): #p1 v2 p3 v4 p5
    if (s >= 39) and (step == 4):
        return True

    if (s < 39 and step == 4) or (s >= 39 and step < 4):
        return False

    moves = [
        f20(s + 1, step + 1),
        f20(s + 3, step + 1),
        f20(s * 2, step + 1)
    ]

    if step % 2 != 0:
        return any(moves)
    return all(moves)


for s in range(1, 39):
    if f20(s):
        print(s)