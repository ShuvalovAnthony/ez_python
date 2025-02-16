for x in range(1000):
    if (
        (10 <= x <= 99) and
        (not x//10 % 2 == 1) and
        (x%3 == 0)
    ):
        print(x)