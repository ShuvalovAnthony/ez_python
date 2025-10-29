from itertools import combinations

# отрезки которые даны
def p(x):
    return 5 <= x <= 280


def q(x):
    return 295 <= x <= 400

def r(x):
    return 375 <= x <= 450

# отрезок который ищем
def a(x, start, stop):
    return start <= x <= stop

# все возможные варианты отрезков
coords = combinations(
    sorted([5, 280, 295, 400, 375, 450]), 2 # !!!!
)

dlini = set() # множество/список всех длин отрезков

for start, stop in coords:
    flag = True

    for x in range(0, 460):
        if not (
            (q(x) <= p(x)) or 
            ((not a(x, start, stop)) <= r(x))
        ):
            flag = False

    if flag:
        dlini.add(stop - start) # !!!! добавляем длину отрезка!!!!


print(min(dlini))