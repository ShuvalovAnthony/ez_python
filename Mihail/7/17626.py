speed = 1966080
time = 280
from math import *
for x in range(1, 10000):
    if (
        ((1280 * 1024 * log2(x)) * 39) / speed
    ) <= time:
        if log2(x) % 1 == 0:
            print(x, log2(x))