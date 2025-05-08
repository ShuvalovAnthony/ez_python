from itertools import permutations


s = "234 136 12 157 467 25 45".split()
v = "BF BD FD FG DA AE GE CE GC".split()


print(*range(1, 8))


for p in permutations("FBDAGCE"):
    if all(str(p.index(a) + 1) in s[p.index(b)] for a, b in v):
        print(*p)

