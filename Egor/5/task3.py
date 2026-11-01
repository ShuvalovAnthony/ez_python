for n in range(10**4, 10**5):
    digits = [int(i) for i in str(n)]
    s = sum(digits)
    m = min(digits) + max(digits)
    l = n//10_000
    r = n%10
    p1 = s - l
    p2 = m - r

    p1, p2 = min([p1, p2]), max([p1, p2])
    z = str(p1) + str(p2)
    if z == "222":
        print(n)