# from functools import lru_cache
# from sys import setrecursionlimit


# setrecursionlimit(10**3)

# @lru_cache()
# def f(n):
#     if n <= 5: return 1000
#     return n + 3 + f(n - 2)


# for i in range(60000):
#     f(i)


# print(3*f(53079) - (f(53077) + f(53075) + f(53073)))


f = [0]*54000

for n in range(54000):
    if n <= 5:
        f[n] = 1000
    else:
        f[n] = n + 3 + f[n - 2]


print(3*f[53079] - (f[53077] + f[53075] + f[53073]))


# speeds = []

# while True:
#     speed = float(input())
#     if speed == 0: break
#     speeds.append(speed)

# print(sum(speeds)/len(speeds))