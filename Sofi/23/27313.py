def f(start, stop):
    if start == stop:
        return 1
    
    # не содержит чисел 20 и 33
    elif (start > stop) or (start in (20, 33)): # если увеличиваем старт - >, уменьш - <
        return 0
    
    moves = [
        f(start + 3, stop),
        f(start + 4, stop),
        f(start*2, stop)
    ]

    return sum(moves)


print(f(3, 15)*f(15, 26)*f(26, 63)) # 15 и 26
print(f(3, 15)*f(15, 63))
print(f(3, 26)*f(26, 63))