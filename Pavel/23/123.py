def f(start, stop):
    if (start < stop) or (start == 8):
        return 0
    if start == stop:
        return 1

    return (
        f(start - 1, stop) + 
        f(start - 4, stop) + 
        f(start // 3, stop)
    )

print(f(19, 14)*f(14, 2))