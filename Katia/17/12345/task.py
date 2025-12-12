f = open(r'Katia/17/12345/17.txt')

data = [int(i) for i in f]

def check(par):
    return (sum(par) %117 == 0)


k = 0

mx = 0
for i in range(len(data) - 1):
    for j in range(i + 1, len(data)):
        par = [data[i], data[j]]
        if check(par):
            k += 1
            mx = max(mx, sum(par))

print(k, mx)