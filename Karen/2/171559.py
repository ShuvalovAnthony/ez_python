from itertools import *

# функция из задачи (логическое выражение)
def f(w, x, y, z):
    return w and (z == (x <= y))


for a in product([0, 1], repeat=5): # repeat = КОЛ_ВО ПРОПУСКОВ
    # все строки (отсчет с НУЛЯ!!!)
    t = [
        (a[0], a[1], 0, 0),
        (0, a[2], a[3], 0),
        (a[4], 1, 1, 1)
    ]

    if len(t) == len(set(t)): # всегда пишем
        for p in permutations("wxyz"): # перестановки всех букв
            if [f(**dict(zip(p, r))) for r in t] == [1, 1, 0]:
                print(*p)