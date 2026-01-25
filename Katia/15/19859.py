from itertools import combinations


p = range(1, 30, 2)

q = range(5, 51, 5)


for i in range(55):
    for a in combinations(range(0, 55), r=i):
        flag = True

        for x in range(0, 55):
            if not (
                ((x in a) <= (x in p)) and
                ((not (x in q)) <= (not (x in a)))
            ):
                flag = False
        
        if flag:
            print(a)
