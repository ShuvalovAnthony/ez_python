for a in range(-100, 100):
    counter = 0 # считаем либо YES либо NO в завис от задачи

    for s, t in [
        (13, 2), (11, 12), (-12, 12), (2, -2), (-10, -10), (6, -5), (2, 8), (9, 10), (1, 13)
    ]:
        if (s > a) or (t > 12):
            counter += 1

    if counter == 4:
        print(a)
        break

