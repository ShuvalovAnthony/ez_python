def f(start, stop, commands=''):
    if (
        (start == stop) and
        ('1111' not in commands) and
        ('2222' not in commands)
    ):
        return 1
    if start > stop:
        return 0
    

    moves = [
        f(start + 1, stop, commands + '1'),
        f(start*2, stop, commands + '2')
    ]

    return sum(moves)

print(f(5, 299))