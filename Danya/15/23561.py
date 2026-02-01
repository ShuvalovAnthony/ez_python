def del_(n, m):
    return n%m == 0

# ищем А
# натурального числа А 

for a in range(1, 10000):
    flag = True

    for x in range(1, 10000):
        # противоположное задаче условие
        # если ИСТИНА должна быть
        # пишем if not
        # это условие для брака нашего a
        if not (
            del_(x, 128) <=
            (
                (not del_(x, a)) <=
                (not del_(x, 80))
            )
        ):
            flag = False
            break

    if flag:
        print(a)
