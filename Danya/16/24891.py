from sys import setrecursionlimit


setrecursionlimit(20000)

def f(n):
    if n <= 10:
        return n
    return n - 7 + f(n - 21)


print(
    (f(185734) - f(185650))//f(40)
)