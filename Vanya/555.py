# from time import time

# start = time()

# for n in range(10**6, 10**6 + 100):
#     summa = 0
#     for i in range(1, n + 1):
#         if n%i == 0:
#             summa += i
    
#     print(n, summa)


# print(time() - start)


# from time import time

# start = time()

# for n in range(10**6, 10**6 + 100):
#     summa = 0
#     for i in range(1, int(n**0.5) + 1):
#         if n%i == 0:
#             summa += i
#             summa += n//i
    
#     print(n, summa)


# print(time() - start)




# # collections Коллекции

# text = "Hello world!"
# nums = [1, 2, 3, 4]
# set_ = {1, 2, 3, 5, 6}
# tuple_ = ("asd", "fsdf", "24")
# r = range(10, 20, 2) # [10, 12, 14, 16, 18]
# geom_progression = [i**2 for i in range(10)]


# for i in geom_progression:
#     print(i)




n = int(input())

for i in range(n):
    s = input()
    print(s, end="_")