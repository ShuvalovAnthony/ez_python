from itertools import product


# for a in range(10**3):
#     flag = True

#     for x, y in product(range(10**3), repeat=2):
#         if not (
#             (x*y < a) or
#             (x < y) or
#             (9 < x)
#         ):
#             flag = False
#             break

#     if flag:
#         print(a)
#         break



def f(a, b, c):
    return a + b + c == 180

def od(n, m):
    del_n = set()

    for i in range(1, int(n**0.5) + 1):
        if n%i == 0:
            if i != 1:
                del_n.add(i)
            del_n.add(n//i)

    for j in range(1, int(m**0.5) + 1):
        if m%j == 0:
            if j in del_n:
                return True
            if m//j in del_n:
                return True
            
    return False


def poz(n, m):
    return n - m > 0


def treug(n, m, k):
    n, m, k = sorted([n, m, k])
    return n + m > k


def cif(x, y):
    return x%10 == y%10


res = []

for a in range(1, 10**3):
    flag = True

    for x, y in product(range(1, 10**3), repeat=2):
        if not (
            (
                (x**2 > 60) or
                (not (x > a))
            ) and
            (
                (not (y**2 > 90)) or
                (y > a)
            )
        ):
            flag = False
            break

    if flag:
        # print(a)
        # break
        res.append(a)

print(len(res))