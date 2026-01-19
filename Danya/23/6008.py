def f(start, stop, commands=""):
    if (start == stop) and ("BCA" in commands):
        return 1
    elif (start > stop):
        return 0

    moves = [
        f(start + 1, stop, commands + "A"),
        f(start*2, stop, commands + "B"),
        f(start*3, stop, commands + "C")
    ]

    return sum(moves)


print(f(2, 27))