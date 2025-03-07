def f(start, stop):
    if (start > stop) or (start == 15): return 0
    if start == stop: return 1

    return (
        f(start + 1, stop) +
        f(start + 3, stop) +
        f(start*3, stop)
    )


print(f(7, 14)*f(14, 20))