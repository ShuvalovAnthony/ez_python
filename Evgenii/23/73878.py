def f(start, stop):
    if (start < stop) or (start == 16): return 0
    if start == stop: return 1

    vars = [f(start - 3, stop)]
    
    if start%2 == 0: vars.append(f(start//2, stop))
    else: vars.append(f(start - 5, stop))

    return sum(vars)


print(f(36, 4))