def f(start, stop):
    if start == stop:
        return 1
    if (start > stop) or (start == 11) or (start == 12): # тк текущее число увеличивается командами
        return 0
    
    moves = [
        f(start + 1, stop),
        f(start*2, stop),
        f(start**2, stop)
    ]

    return sum(moves)


print(f(2, 10)*f(10, 40))