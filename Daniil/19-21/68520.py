def f(s1, s2, m, n=2021):
    if (s1 + s2) >= 59: return m%2 == 0 # vanya win
    if m == 0: return 0

    moves = [
        f(s1 + 1, s2, m - 1),
        f(s1*2, s2, m - 1),
        f(s1, s2 + 1, m - 1),
        f(s1, s2*2, m - 1),
    ]

    if n == 19: return any(moves)

    return any(moves) if m%2 else all(moves)


print(min([s for s in range(1, 54) if (not f(s, 5, 1, 19)) and f(s, 5, 2, 19)]))
print(sorted(
    [s for s in range(1, 54) if ((not f(s, 5, 1)) and f(s, 5, 3) and (not f(s, 5, 2)))]
))
print(min(
    [s for s in range(1, 54) if (
        (f(s, 5, 4) and (not f(s, 5, 2)) and (not f(s, 5, 1)) and (not f(s, 5, 3)))
    )]
))