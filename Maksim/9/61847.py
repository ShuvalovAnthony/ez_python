# Все пункты и дороги куда они ведут
s = "АГВБ БЖ ВДЕБЖ ГДВ ДЕЗ ЕЗ ЖЗ З"

d = {i[0]:i[1:] for i in s.split()}

f = lambda a, b: (a == b) + sum(f(c, b) for c in d[a])

# все пути из А в З
print(f("А", "З"))