def f(a, b):
    if (a > b) or (a in (9, 15)): return 0
    elif (a == b): return 1
    return f(a + 1, b) + f(a + 3, b) + f(a*3, b)


print(f(3, 18))