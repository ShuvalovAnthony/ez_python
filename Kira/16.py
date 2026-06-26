def f(n):
    if n <= 2:
        return 2
     
    return 3*f(n - 1) - f(n - 2)


print(f(6))