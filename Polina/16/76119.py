# from sys import setrecursionlimit
# from functools import lru_cache

# setrecursionlimit(10000)


# def f(n):
#     if n >= 10000: return 1
#     if n%2 == 0: return 2*n + f(n + 1)
#     return f(n + 2) + n


# print(f(2022) - f(2025))


f = [0]*2060


for n in range(2050, 0, -1):
    if n >= 10000:
        f[n] = 1
    elif (n < 10000) and (n%2 == 0):
        f[n] = 2*n + f[n + 1]
    else:
        f[n] = f[n + 2] + n


print(f[2022] - f[2025])