from itertools import product, permutations, combinations


# for word in product("023456789", repeat=5):
#     word = ''.join(word)
#     print(word)


# def check(word: str):
#     for i in "246":
#         word = word.replace(i, "0")
#     for i in "57":
#         word = word.replace(i, "3")
    
#     return ("00" not in word) and ("33" not in word)

# counter = 0

# for word in permutations("0234567", r=5):
#     word = ''.join(word)
#     if (word[0] != '0') and check(word):
#         counter += 1

# print(counter)



# intervals = combinations(
#     sorted([432, 543, -543, 23, -23, 123, 7]),
#     r=2
# )

# print(intervals)

# for interval in intervals:
#     print(interval)


# from random import randint
# from time import time

# k = 500
# nums1 = (1,)*k
# nums2 = (2,)*k
# nums3 = (3,)*k

# res = []
# start = time()

# for n1 in nums1:
#     for n2 in nums2:
#         for n3 in nums2:
#             res.append(n1 + n2 + n3)

# stop = time()
# print(stop - start)