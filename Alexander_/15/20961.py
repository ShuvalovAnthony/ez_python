from itertools import*

def p(x):
    return 15<=x<=142

def q(x):
    return 38<=x<=167

def a(x, start, stop):
    return start<=x<=stop

dl=set()

intervals=combinations(sorted([15, 142, 38, 167]), r=2)

for start, stop in intervals:
    flag=True

    for x in range(1, 5000):
        if (
            not(((q(x)))<=(( (not(a(x, start, stop))) and(p(x))) <= (not(q(x))) ))
            ):
            flag=False
            
    if flag:
        dl.add(stop-start)
print(dl)