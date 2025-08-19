# 9 zadacha
f = open("Katia/vars/19_08_25/9.txt")

data = [
    [int(i) for i in row.split()] for row in f
]


def check(row: list):
    triple = []
    unique = []

    for num in row:
        if row.count(num) == 3:
            triple.append(num)
        if row.count(num) == 1:
            unique.append(num)

    return (
        (len(triple) == 3 and len(unique) == 3) and
        (triple[0] > sum(unique)/3)
    )


for i in range(len(data)):
    row = data[i]

    if check(row):
        print(i + 1)





# # 17 zadacha
# f = open("Katia/vars/19_08_25/17_23201.txt")

# nums = [int(i) for i in f]


# for num in sorted(nums):
#     if (100 <= num <= 999) and (num%10 == 7):
#         min_ok_na_7 = num
#         break


# def check(pair: list):
#     return (
#         (
#            (pair[0] in range(100, 1000) and pair[1] not in range(100, 1000)) or
#            (pair[0] not in range(100, 1000) and pair[1] in range(100, 1000))
#         ) and
#         (
#             sum(pair)%min_ok_na_7 == 0
#         )

#     )

# count = 0
# min_summa = 10**6


# for i in range(len(nums) - 1):
#     pair = nums[i:i+2]

#     if check(pair):
#         count += 1
#         min_summa = min(min_summa, sum(pair))

# print(count, min_summa)



# def f(start, stop):
#     if (start < stop) or (start == 13): return 0
#     if start == stop: return 1

#     return (
#         f(start - 1, stop) +
#         f(start - 2, stop) +
#         f(start//3, stop)
#     )


# print(f(19, 6)*f(6, 4))

# from sys import setrecursionlimit

# setrecursionlimit(15000)


# def f(n):
#     if n < 10: return n
#     if n >= 10: return 3*n + f(n - 3)



# print(
#     (f(6250) + 2*f(6244))//f(6238)
# )


# for a in range(200):
#     flag = True

#     for x in range(200):
#         for y in range(200):
#             if not (
#                 (x*y > a) or (x > y) or (11 > x)
#             ):
#                 flag = False

#     if flag:
#         print(a)


# def to_9(num: int):
#     res = ''
#     while num > 0:
#         res += str(num%9)
#         num //= 9
    
#     return res[::-1]

# for x in range(1, 3001):
#     exp = 9**150 + 9**30 - x

#     res = to_9(exp)

#     if res.count("0") == 122:
#         print(x)
#         break



# def to_25(num: int):
#     alph = "0123456789ABCDEFGHIJKLMN"

#     res = ''

#     while num > 0:
#         res += alph[num%25]
#         num //= 25

#     return res[::-1]


# print(to_25(345678))





# def algo(s: str):
#     while ("78" in s) or ("688" in s) or ("8888" in s):
#         if "78" in s:
#             s = s.replace("78", "8", 1)
#         if "688" in s:
#             s = s.replace("688", "87", 1)
#         if "8888" in s:
#             s = s.replace("8888", "6", 1)

#     return s


# for n in range(4, 10000):
#     s = "7" + "8"*n

#     s = algo(s)
#     # генератор
#     summa_cifr = sum([int(i) for i in s])

#     if summa_cifr == 61:
#         print(n)
#         break


# from itertools import product

# index = 1


# for word in product(sorted("ТЕОРИЯ"), repeat=6):
#     word = ''.join(word)

#     if (
#         (index%2 == 1) and
#         (word[0] not in "РТЯ") and 
#         (word.count("И") >= 2)
#     ):
#         print(index, word)

#     index += 1




# for n in range(1000):
#     bin_n = bin(n)[2:] # "0b10101010"

#     if n%3 == 0:
#         bin_n += bin_n[-3:]
#     else:
#         bin_n += bin(n%3*3)[2:]

#     r = int(bin_n, 2)

#     if r < 130:
#         print(n)
