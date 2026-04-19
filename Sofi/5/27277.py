def to_3(num):
    res = ''

    while num > 0:
        res += str(num%3)
        num //= 3

    return res[::-1]


delta = 10**6
answ = 0


for n in range(1, 10000):
    tri_n = to_3(n) # 12010210200 str

    if n%3 != 0:
        tri_n = '1' + tri_n + tri_n[-3:]
    else:
        summa_cifr = sum([int(i) for i in tri_n])

        tri_n += to_3(summa_cifr*8)

    r = int(tri_n, 3)

    if abs(1220 - r) < delta:
        delta = abs(1220 - r)
        answ = r

print(answ)



# 2 sposob

# def to_3(num):
#     res = ''

#     while num > 0:
#         res += str(num%3)
#         num //= 3

#     return res[::-1]


# res = []


# for n in range(1, 10000):
#     tri_n = to_3(n) # 12010210200 str

#     if n%3 != 0:
#         tri_n = '1' + tri_n + tri_n[-3:]
#     else:
#         summa_cifr = sum([int(i) for i in tri_n])

#         tri_n += to_3(summa_cifr*8)

#     r = int(tri_n, 3)

#     res.append(
#         [abs(1220 - r), r]
#     )


# res = sorted(res, key=lambda x: x[0])


# for row in res[:10]:
#     print(row)