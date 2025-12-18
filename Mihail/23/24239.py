from sys import setrecursionlimit

setrecursionlimit(3000000)

def f(start, stop):
    if start == stop:
        return 1
    elif start > stop or start == 7:
        return 0
    
    moves = [
        f(start + 1, stop),
        f(start + 2, stop),
        f(start * 3, stop)
    ]
    
    return sum(moves)


print(f(1, 10)*f(10, 25))