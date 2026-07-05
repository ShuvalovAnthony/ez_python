def f(start, stop):
    if start == stop:
        return 1
    
    if start < stop: #  or start == 11 - траектория НЕ содержит 11
        return 0
    
    moves = [
        f(start - 1, stop),
        f(start//2, stop)
    ]

    return sum(moves)


print(f(40, 17)*f(17, 6)) # от 40 к 6 с ОБЯЗАТЕЛЬНЫМ проходом через 17