from sys import setrecursionlimit


setrecursionlimit(100000)

def f(n):
    if n == 1:
        return 1
    return n**3 + f(n - 1)


def g(n):
    if n < 10:
        return 2*n
    return g(n - 2) + 1


print(
   f(2025) - f(2022)
)

