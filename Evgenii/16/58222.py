def f(n):
    if n < 3: return 1
    if n%2: return f(n - 1) + 3*f(n - 2)
    return sum([f(i) for i in range(1, n)])


print(f(28))