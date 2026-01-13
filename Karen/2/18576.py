from itertools import *

def f(w,x,y,z):
    return (not (w <= (x == (y or y)))) and (z <= x)

for a in product([0, 1], repeat=5): #repeat - колво пропусков в таблице
    t = [
        (a[0], 1, 1, a[1]),
        (0, a[2], a[3], 0),
        (a[4], 0, 1, 0)
    ]

    if len(t)==len(set(t)): #ВСЕГДА ПИШЕМ
        for p in permutations("xywz"): #перебираем комбинации
            if [f(**dict(zip(p, r))) for r in t]==[1, 1, 1]:
                print(*p)