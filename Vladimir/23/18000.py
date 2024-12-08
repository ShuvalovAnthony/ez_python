def div_sum(num):
    summa = 0
    for i in range(1, num + 1):
        if num%i == 0: summa += i
    return summa


def f(a, b):
    if (a > b): return 0
    elif (a == b): return 1
    return f(a + 1, b) + f(div_sum(a), b)


print(f(2, 24))