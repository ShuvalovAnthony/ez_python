def treug(n, m, k):
    n, m, k = sorted([n, m, k])
    return n + m > k


# (ТРЕУГ(x, 10, 20) → (¬(МАКС(x, 8) > 24))) = ¬(ТРЕУГ( 3, A, x))


for a in range(1, 100):
    flag = True

    for x in range(1, 100):
        if not (
            treug(x, 10, 20) <=
            (
                (not (
                    max(x, 8) > 24
                )) ==
                (not treug(3, a, x))
            )
        ):
            flag = False
            break

    if flag:
        print(a)