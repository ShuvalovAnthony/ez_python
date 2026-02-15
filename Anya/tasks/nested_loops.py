n = int(input())

for multiplicator in range(n):
    for delta in range(1, n + 1):
        if delta != n:
            print(multiplicator*n + delta, end="\t")
        else:
            print(multiplicator*n + delta)
