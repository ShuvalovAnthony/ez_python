def del_(n, m):
    return n%m == 0


count = 0

for a in range(1, 1000):
    flag = True

    for x in range(1, 1000):
        if not (
            del_(x, a) or (
                (170 <= x <= 220) <=
                (not del_(x, 24)) # x in range(170, 221)
            )
        ):
            flag = False


    if flag:
        count += 1


print(count)
