def f(start, stop):
    if (start < stop) or (start == 16): return 0
    if start == stop: return 1

    return f(start - 3, stop) + f(start//2 if start%2 == 0 else start - 5, stop)


print(f(36, 4))



