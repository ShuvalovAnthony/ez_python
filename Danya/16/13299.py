def f(n):
    if n <= 3: 
        return 1
    elif n%3 == 0:
        return f(n//3) + 4*n
    return n**3 - 26


for n in range(1, 10**5):
    if f(n) < 300:
        print(n)