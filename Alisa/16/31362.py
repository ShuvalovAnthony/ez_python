from sys import setrecursionlimit


setrecursionlimit(50_000)


def f(n):
    if n == 1:
        return 1

    return (n + 1)*f(n - 1)


print(
    (f(42038) + 3*f(42037))//f(42036)
)