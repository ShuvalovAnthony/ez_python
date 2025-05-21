from itertools import permutations


vars = []

for p in permutations("SSSCCKK", r=3):
    vars.append(''.join(p))

vars = list(set(vars))

print(vars.count("SSS"), len(vars))