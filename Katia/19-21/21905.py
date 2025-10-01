def f19(s, step=1): #1p 2v 3p 4v 5p
    if (step == 3) and (s >= 67):
        return 1
    
    if (
        (step == 3 and s < 67) or 
        (step < 3 and s >= 67)
    ): return 0 

    moves = [
        f19(s+1, step +1),
        f19(s+4, step + 1),
        f19(s*3, step +1)
    ]

    if step %2 == 1:
        return all(moves)
    return any(moves)

for s in range(1, 66):
    if f19(s):
        print(s)