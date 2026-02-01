def f(s1, s2, step = 1): #p1 v2 p3 v4 p5
    if s1 >= 479 and step == 3 or (s2 >= 479 and step == 3):
        return True
    if ((s1 < 479 and step == 3) or (s1 >= 479 and step < 3)) or ((s2 < 479 and step == 3) or (s2 >= 479 and step < 3)):
        return False
    moves = [
        f(s1 +1, step + 1),
        f(s2 +1, step + 1),
        f(s1 +3, step + 1),
        f(s2 +3, step + 1),
        f(s1 * 2, step + 1),
        f(s2 * 2, step + 1),
    ]
    if step % 2 == 0:
        return any(moves)
    return all(moves)

for s2 in range(1, 479):
    if f(239, s2):
        print(s2)