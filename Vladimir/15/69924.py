def del_(n, m):
    return n%m == 0

def b(x):
    return 70 <= x <= 90


for a in range(100, 0, -1):
    flag = True

    for x in range(1, 100):
        if not (
            del_(x, a) or 
            (
                b(x) <=
                (not del_(x, 27))
            )
        ):
            flag = False
    
    if flag:
        print(a)
        break