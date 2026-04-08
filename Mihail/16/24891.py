f = [0]*190_000

for n in range(190_000):
    if n <= 10:
        f[n] = n
    elif n <= 21:
        f[n] = n - 7 + (n - 21)
    else:
        f[n] = n - 7 + f[n - 21]

print(
    (f[185734] - f[185650])/f[40]
)