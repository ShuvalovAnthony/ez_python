f = [0]*3000


for n in range(2100, -1, -1):
    if n >= 2025:
        f[n] = n
    else:
        f[n] = 2*n + f[n + 2]


print(
    f[82] - f[81]
)