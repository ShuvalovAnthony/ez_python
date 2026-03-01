def f(start, stop):
    if start == stop:
        return 1
    elif start > stop or start == 8: # исключающий этап
        return 0
    
    moves = [
        f(start + 1, stop),
        f(start + 2, stop),
        f(start*2, stop)
    ]

    return sum(moves)


print(f(3, 14)*f(14, 18)) # 14 - обязательный этап