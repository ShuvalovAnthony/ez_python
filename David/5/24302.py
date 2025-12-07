def convert(n: int, base: int):
    res = ''

    while n > 0:
        res += str(n%base)
        n //= base
    
    return res[::-1]


def summa_cifr(n: str):
    return sum([int(i) for i in n])

answ = []

for n in range(167, 1000):
    tri_n = convert(n, 3)

    if summa_cifr(tri_n)%9 == 0:
        tri_n += '2'
    else:
        tri_n += convert(summa_cifr(tri_n)%9, 3)

    r = int(tri_n, 3)

    answ.append(r)

print(min(answ))




# ПЛОХОЙ СПОСОБ

# answ = []

# for n in range(167, 10000):
#     tri_n = ''

#     while n > 0:
#         tri_n += str(n%3)
#         n //= 3

#     tri_n = tri_n[::-1]

#     summa_cifr = tri_n.count("1") + tri_n.count("2")*2

#     if summa_cifr%9 == 0:
#         tri_n += '2'
#     else:
#         ostatok = summa_cifr%9

#         tri_ostatok = ''

#         while ostatok > 0:
#             tri_ostatok += str(ostatok%3)
#             ostatok //= 3
        
#         tri_ostatok = tri_ostatok[::-1]

#         tri_n += tri_ostatok

#     r = int(tri_n, 3)

#     answ.append(r)

# print(min(answ))
