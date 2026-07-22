def f(start, stop):
    if start == stop:
        return 1
    elif start < stop or start == 7: # ‼️ or + знак избегаемый этап
        return 0

    moves = [
        f(start - 1, stop), # ‼️ не забываем f
        f(start - 4, stop),
        f(start//3, stop)
    ]

    return sum(moves)

# обязательный/ые этапы разбивают общий путь на отрезки
print(
    f(19, 13)*f(13, 2)
)

