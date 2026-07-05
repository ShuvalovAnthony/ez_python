from sys import setrecursionlimit, set_int_max_str_digits


setrecursionlimit(30_000)

def f(n):
    if n == 1:
        return 1
    
    return n*f(n - 1)


print(
    (f(2024) - 5*f(2023) + 10**45000)/f(2022)
)