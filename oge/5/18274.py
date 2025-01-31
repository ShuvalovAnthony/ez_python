from itertools import product


for path in product([1, 2], repeat=5): # repeat = КОЛВУ ДЕЙСТВИЙ

    n = 76

    for step in path:
        if step == 1:
            n /= 2
        else:
            n -= 3

    if n == 5:
        print(path)