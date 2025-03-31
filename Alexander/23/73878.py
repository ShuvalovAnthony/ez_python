def f(start, stop):
    if (start < stop) or (start == 16): return 0
    if start == stop: return 1

    if start%2 == 0:
        return f(start - 3, stop) + f(start//2, stop)
    else:
        return f(start - 3, stop) + f(start - 5, stop)
    


print(f(36, 4))