def f(start, stop, commands=""):
    if (start == stop) and ("BACA" not in commands):
        return 1
    elif (start > stop) or (start == 28): # где return 0 
        return 0                          # через or ИЗБЕГАЕМЫЙ ЭТАП
        
    moves = [
        f(start + 2, stop, commands + "A"),
        f(start + 3, stop, commands + "B"),
        f(start*2, stop, commands + "C")
    ]

    return sum(moves)


print(f(2, 40))