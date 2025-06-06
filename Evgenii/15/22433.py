for a in range(250):
    fl=True
    for x in range(250):
        f=(x&117 != 0) and (x&91 == 0) <= (not (x&a == 0))
        if f==0:
            fl=False
    if fl:
        print(a)
        break