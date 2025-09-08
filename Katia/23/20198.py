def f(start, stop, counter=0):
    if (start > stop + 5) or (counter > 2): return 0
    elif start == stop: return 1

    return (
        f(start - 1, stop, counter + 1) +
        f(start + 5, stop) +
        f(start*2, stop)
    )

print(f(5, 34))
