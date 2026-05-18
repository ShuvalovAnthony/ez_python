from sys import setrecursionlimit

setrecursionlimit(10**6)


def f(n):
    if n >= 14:
        return n*f(n - 1)
    return 8*g(n - 3)

def g(n):
    if n < 31:
        return 4
    return n//2*g(n - 2)


print(
    f(320727)//g(641452)
)