from itertools import product


for path in product([1, 2], repeat=5):
    num = 76

    for step in path:
        if step == 1:
            num = num / 2
        elif step == 2:
            num = num - 3

    if num == 5:
        print(*path)