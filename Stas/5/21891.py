res = []

for n in range(1, 1000):
    n_2 = bin(n)[2:]

    for _ in range(2):
        n_2 += str(n_2.count("1")%2)

    r = int(n_2, 2)

    if r > 253:
        # print(n)
        # break

        res.append(n)

print(min(res))