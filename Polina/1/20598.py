from itertools import permutations

s = "27 1467 457 236 37 24 1235".split()
v = "АЕ ЕБ БЖ ЕЖ ЖД ЖГ ДГ ГВ АВ ЕВ".split()

print(*range(1, 8))

for p in permutations("АЕБЖДГВ"):
    if all(str(p.index(a) + 1) in s[p.index(b)] for a, b in v):
        print(*p)