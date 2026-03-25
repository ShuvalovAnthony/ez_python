from sys import setrecursionlimit

setrecursionlimit(10000)

def f(n):
    if n < 5:
        return 11
    return 11*f(n - 6)


print(f(41387)/11**6897)