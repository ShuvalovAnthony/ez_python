# from sys import setrecursionlimit


# setrecursionlimit(5000)


# def f(n):
#     if n < 3: return n
#     return (n - 1)*f(n - 2)


# print(
#     (f(2025) - f(2023))/f(2021)
# )


f = [0]*2060

for n in range(2050):
    if n < 3: f[n] = 3
    else: f[n] = (n - 1)*f[n + 2]


print(
    (f[2025] - f[2023])/f[2021]
)