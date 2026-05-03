# from sys import setrecursionlimit


# setrecursionlimit(100_000)


# def f(n):
#     if n < 10:
#         return 1
#     return (n + 3)*f(n - 3)


# print(
#     (f(247563)//519 - 477*f(247560))//f(247557)
# )



f = [0]*250_000

for n in range(250_000, -1, -1):
    if n < 10:
        f[n] = 1
    else:
        f[n] = (n + 3)*f[n - 3]


print(
    (f[247563]//519 - 477*f[247560])//f[247557]
)
