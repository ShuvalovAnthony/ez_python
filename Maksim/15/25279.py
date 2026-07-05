from itertools import combinations

# все функции отрезков + отрезок А
def p(x):
    return 66 <= x <= 67

def o(x):
    return 32 <= x <= 125

def t(x):
    return 30 <= x <= 491

def a(x, start, stop):
    return start <= x <= stop

# все комбинации отрезков
vars = combinations(
    sorted([66, 67, 32, 125, 30, 491]), # !!! sorted
    r=2
)

# все длины отрезков, которые подошли
dlini = set()

for start, stop in vars:
    flag = True

    for x in range(20, 500):
        if not (
            (not a(x, start, stop)) <=
            (
                p(x) or
                (not o(x)) or
                (not t(x))
            )
        ):
            flag = False

    if flag:
        dlini.add(stop - start) # stop - start = длина


print(min(dlini))