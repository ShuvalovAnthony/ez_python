m = []
for x in range(1, 2031):
    a = 6**2030 + 6**100 - x
    k = 0
    while a > 0:
        if a % 6 == 0:
            k += 1
        a //= 6
    m.append(k)
print(min(m))