from itertools import product, permutations, combinations
from string import digits, ascii_uppercase
from sys import setrecursionlimit


# setrecursionlimit(5000)
# 2

# def f(x, y, w, z):
#     return x and (z <= w) and (not y)


# for a in product([0, 1], repeat=7):
#     table = [
#         (a[0], a[1], 1, a[2]),
#         (a[3], 1, 0, a[4]),
#         (1, 0, a[5], a[6])
#     ]

#     for p in permutations("xywz"):
#         if len(table) == len(set(table)):
#             if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
#                 print(*p)


# 5

# for n in range(1, 10000):
#     bin_n = bin(n)[2:]

#     if bin_n.count('1')%2 == 0:
#         bin_n += '0'
#         bin_n = '10' + bin_n[2:]
#     else:
#         bin_n += '1'
#         bin_n = '11' + bin_n[2:]

#     r = int(bin_n, 2)

#     if r > 480:
#         print(n)
#         break


# words = set()

# for word in product("ДГИАШЭ", repeat=5):
#     word = ''.join(word)

#     if (
#         (word[0] not in 'ИАЭ') and
#         (word[-1] not in 'ДГШ')
#     ):
#         words.add(word)

# print(len(words))


# f = open("Polina/vars/9.txt")

# data = [
#     [int(i) for i in row.split()] for row in f
# ]


# def check(row: list):
#     povtor = []
#     unique = []

#     for num in row:
#         if row.count(num) == 3:
#             povtor.append(num)
#         elif row.count(num) == 1:
#             unique.append(num)

#     return (
#         (len(unique) == 1) and
#         (len(povtor) == 6) and
#         (max(povtor) > unique[0])
#     )


# counter = 0


# for row in data:
#     if check(row):
#         counter += 1

# print(counter)


# 13



# mask = '255.255.255.240'
# ip = '143.168.72.213'


# bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split('.')]
# bin_ip = [bin(int(i))[2:].zfill(8) for i in ip.split('.')]


# print(bin_mask)
# print(bin_ip)


# ['11111111', '11111111', '11111111', '1111   0000']
# ['10001111', '10101000', '01001000', '11011110']

# 14316872222

# print(int('11011110', 2))


# 14

# alph = digits + ascii_uppercase[:11]


# for x in alph:
#     res = (
#         int('82934' + x + '2', 21) +
#         int('2924' + x + x + '7', 21) +
#         int('67564' + x + '8', 21)
#     )

#     if res%20 == 0:
#         print(res//20)
#         break


# 15

# for a in range(100):
#     flag = True

#     for x, y in product(range(100), repeat=2):
#         if not (
#             (5 < y) or
#             (x > 32) or
#             (x + 2*y < a)
#         ):
#             flag = False
#             break

#     if flag:
#         print(a)
#         break


# 16



# def f(n):
#     if n <= 5: return 1
#     return n + f(n - 2)


# print(f(2126) - f(2122))



# 17

# f = open("Polina/vars/17_21416.txt")

# nums = [int(i) for i in f]


# summa_negative = sum([i for i in nums if i < 0])


# def check(troika: list):
#     return (
#         (max(troika)*min(troika) > summa_negative)
#     )

# counter = 0
# max_summa = 0

# for i in range(len(nums) - 2):
#     troika = [nums[i], nums[i + 1], nums[i + 2]]

#     if check(troika):
#         counter += 1
#         max_summa = max(
#             max_summa,
#             sum(troika)
#         )


# print(counter, max_summa)



# 23

# def f(start, stop):
#     if (start > stop) or (start == 35): return 0
#     if start == stop: return 1

#     moves = [
#         f(start + 1, stop),
#         f(start + 2, stop),
#         f(start*2, stop)
#     ]

#     return sum(moves)


# print(f(7, 13)*f(13, 15)*f(15, 51))


# 25

# def func(n: int):
#     deliteli = set()

#     for i in range(1, int(n**0.5) + 1):
#         if n%i == 0:
#             # i
#             if (i%10 == 7) and (i != 7):
#                 deliteli.add(i)

#             # n//i
#             if (n//i%10 == 7) and (n//i != n):
#                 deliteli.add(n//i)

#     if deliteli: return min(deliteli)
#     return False


# limit = 5

# for num in range(1_125_001, 10**12):
#     res = func(num)

#     if res:
#         print(num, res)
#         limit -= 1

#     if limit == 0:
#         break