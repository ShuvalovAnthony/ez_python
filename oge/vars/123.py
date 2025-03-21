from time import time
from random import randint


start = time()

nums = []

for i in range(10**7):
    n = randint(1, 100)
    # print(n)
    nums.append(n)

stop = time()

print("Total time:", stop - start)

