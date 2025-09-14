def f(start, stop):
    if start == stop:
        return 1
    
    if (start < stop) or (start == 3):
        return 0
    
    return (
        f(start - 1, stop) +
        f(start - 2, stop)
    )


print(f(7, 1))
