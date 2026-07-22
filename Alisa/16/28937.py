from sys import setrecursionlimit


setrecursionlimit(50_000)


def f(n):
    if n >= 21:
        return f(n - 8) + 1095
    return 10*(g(n - 7) - 36)

def g(n):
    if n >= 22560:
        return n/23 + 33
    return g(n + 11) - 4


print(
    f(548)
)