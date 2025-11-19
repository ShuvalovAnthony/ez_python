from itertools import *

# функция из задачи (логическое выражение)
def f(w, x, y, z):
    return (x and (not z)) or (y == z) or (not w)


for a in product([0, 1], repeat=4): # repeat = КОЛ_ВО ПРОПУСКОВ
    # все строки (отсчет с НУЛЯ!!!)
    t = [
        (a[0], a[1], 0, 0),
        (1, 0, a[2], 0),
        (1, 0, 1, a[3])
    ]

    if len(t) == len(set(t)): # всегда пишем
        for p in permutations("wxyz"): # перестановки всех букв
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                print(*p)