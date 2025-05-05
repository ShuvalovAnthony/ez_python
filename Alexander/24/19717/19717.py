f = open("Alexander/24/19717/24.5_19717.txt").read()


f = f.split("M")

max_len = 0

for i in range(len(f) - 278):
    sub = "M".join(f[i:i + 279])
    max_len = max(max_len, len(sub))


print(max_len)