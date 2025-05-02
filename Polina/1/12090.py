from itertools import permutations

s = "457 469 6789 129 1 239 138 379 23468".split()
v = "ПА ПЗ ПО ПД АО АЛ ЮЛ ВЛ ВР ВД РЗ РД ДЗ".split()

print(*range(1, 10))

for p in permutations("ПОАЛЮДВРЗ"):
    if all(str(p.index(a) + 1) in s[p.index(b)] for a, b in v):
        print(*p)
