def f(n):
    if n == 0: return 1
    if n%2: return (n%10)*f(n//100)
    return f(n//100)

counter = 0


for n in range(10**7, 9*10**7 + 1):
    if f(n) == 25:
        counter += 1

print(counter)

