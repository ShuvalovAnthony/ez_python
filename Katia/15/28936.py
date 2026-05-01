for a in range(5*485*485 - 10, 5*485*485 + 10):
    flag = True

    for x in range(486):
        for y in range(5*486):
            if not (
                (x*y < a) or (5*x < y) or (486 <= x)
            ):
                flag = False
                break
    
    if flag:
        print(a)
    