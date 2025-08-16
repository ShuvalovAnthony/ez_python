for a in range(-1000, 1000):    
    counter = 0

    for s, t in [
        (1, 2), (11, 2), (1, 12), (11, 12), (-11, -12), (-11, 12), (-12, 11), (10, 10), (10, 5)
    ]:
        if (s > 10) or (t > a):
            ...
        else:
            counter += 1

    if counter == 3:
        print(a)


