from itertools import permutations

def f(a, b, c, d): # *args
    return (f"a={a}, b={b}, c={c}, d={d}")


params = {
    "d":7,
    "c":1,
    "b":2,
    "a":3
}

print(f(**params))


# for row in permutations([1, 2, 3, 4], r=4):
#     print(f(*row), row)


# **kwargs - key word arguments именованные аргументы