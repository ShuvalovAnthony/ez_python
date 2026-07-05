for x in range(1, 1000):
    if not (
        (x > 3) or not ((x < 4) and (x > 2))
    ):
        print(x)
        break