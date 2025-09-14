for x in range(1, 1000):
    if not (
        (not x < 6) or
        (
            (x < 5) and (x >= 4)
        )
    ):
        print(x)