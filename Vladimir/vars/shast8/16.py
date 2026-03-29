f = [0]*10**7


for n in range(10**7):
    if n < 20:
        f[n] = 10
    elif n%2 == 0:
        f[n] = f[n//2] + n - 3
    else:
        f[n] = f[n - 2] + 6


for n in range(len(f)):
    if 1_000_0000 <= f[n] <= 9_999_9999:
        print(f[n], n)
        break