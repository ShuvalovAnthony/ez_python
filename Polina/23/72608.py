def f(start, stop):
    if start < stop: return 0
    if start == stop: return 1
    return f(start - 2, stop) + f(start//2, stop) +\
        f(start//3, stop)


print(f(38, 12)*f(12, 3))
