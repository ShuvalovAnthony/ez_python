# 1 1 2 3 5 8 13...
# 1 2 3 4 5 6 7

from functools import lru_cache


last = 1
prelast = 1

for i in range(1, 50):
    if i <= 2: print(1)
    else:
        temp = last + prelast
        print(temp)
        prelast = last
        last = temp