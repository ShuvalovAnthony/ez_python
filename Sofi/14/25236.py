for p in range(11, 37):
    for x in range(1, 500_001):
        left = int("29A1", p) + int("47771", p) + int("12A", p)
        # left = 2*p**3 + 9*p**2 + 10*p + 1
        right = 1_000_000 + x

        if left == right:
            print(p)