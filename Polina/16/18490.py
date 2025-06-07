f = [0]*3500


for n in range(3499, -1, -1):
    if n > 3000:
        f[n] = n
    else:
        f[n] = (2*n + 4)*f[n + 2]


print(f[20]/f[28])


