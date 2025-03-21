def f(s1, s2, m, n=2021):
    if (s1 + s2) > 60: return m%2 == 0 # vanya win
    if m == 0: return 0

    s1, s2 = min(s1, s2), max(s1, s2)

    moves = [
        f(s1 + 1, s2, m -1),
        f(s1 + 2, s2, m -1),
        f(s1*2, s2, m -1),
    ]

    if n == 19: return any(moves)

    return any(moves) if m%2 else all(moves)


print(min([s for s in range(1, 53) if (
    (not f(8, s, 1)) and f(8, s, 2)
)]))


# any - победа в ИГРЕ (а не игрока)

# если петя должен выиграть то any для пети - лучший ход
# а для вани any - худший ход

# all - 