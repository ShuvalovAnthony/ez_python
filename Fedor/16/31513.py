from sys import setrecursionlimit


setrecursionlimit(30000)

def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n*f(n - 1)


print(
    (f(3038) + 5*f(3037))/f(3036)
)