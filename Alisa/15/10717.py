def treug(n, m, k):
    ...


for a in range(1, 1000):
    flag = True

    for x in range(1, 1000):
        if not (    
            not (
                (treug(x, 11, 18) == (
                    not (max(x, 5) > 68)
                )) and
                treug(x, a, 5)
            )
        ):
            flag = False

    if flag:
        print(a)