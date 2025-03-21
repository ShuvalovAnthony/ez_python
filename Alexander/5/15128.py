for n in range(9999, 999, -1):
    n = str(n)
    sum_12 = int(n[0]) + int(n[1]) # int
    sum_23 = int(n[1]) + int(n[2])
    sum_34 = int(n[2]) + int(n[3])

    summi = sorted([sum_12, sum_23, sum_34])[1:]

    res = ''.join([str(i) for i in summi]) # str

    if res == "1315":
        print(n)
        break