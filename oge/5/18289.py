from itertools import product

for path in product([1, 2], repeat=5): # все возможные пути
    n = 65 # начальное число ИЗ УСЛОВИЯ

    for step in path:
        if step == 1: # по первому пути - первое действие ИЗ УСЛОВИЯ
            n /= 2
        else: # второй путь и второе действие ИЗ УСЛОВИЯ
            n -= 1
         
    if n == 4: # равенство из условия
        print(path)