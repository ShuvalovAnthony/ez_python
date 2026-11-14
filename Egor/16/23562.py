from sys import setrecursionlimit


setrecursionlimit(30_000)


def f(n):
    return g(n - 1)

def g(n):
    if n <= 9:
        return 3*n
    return g(n - 2) + 1


print(
    f(47995)
)