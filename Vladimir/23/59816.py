def f(a, b): # a - текущее число, b - куда идем по условию задачи
    if (a > b) or (a == 15): return 0
    elif (a == b): return 1
    return f(a + 1, b) + f(a + 3, b) + f(a*3, b)


print(f(7, 14)*f(14, 20))
