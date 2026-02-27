# def tri(num):
#     s = ''
#     while num>0:
#         s += str(num%3)
#         num //= 3
#     return s[::-1]
# for num in range(1, 10000000):
#     trin = tri(num)
#     trin = trin.replace('0', '*')
#     trin = trin.replace('2', '0')
#     trin = trin.replace('*', '2')
#     trin = int(trin)
#     r = int(str(trin), 3)
#     if r == 1864246:
#         print(abs(num-r))
#         break
#
# from itertools import *
# k = 0
# for num in product('123456789ABCD', repeat=6):
#     num = ''.join(num)
#     if num.count('4') >= 1 and ((num[0] in 'BCD' and num[1] in 'BCD') + (num[1] in 'BCD' and num[2] in 'BCD') + (num[2] in 'BCD' and num[3] in 'BCD') + (num[3] in 'BCD' and num[4] in 'BCD') + (num[4] in 'BCD' and num[5] in 'BCD')) == 1:
#         k += 1
# print(k)

# def f(start, stop):
#     if start > stop or start == 30:
#         return 0
#     elif start == stop:
#         return 1
#     return (
#         f(start+1, stop)+
#         f(start*2, stop)+
#         f(start*3, stop)
#            )
#
# print(f(2, 12)*f(12,36))

# def f(x,y,w,z):
#     return (x <= (z<=w)) and (z<= (y== (not w)))
#
# for a in product ([0,1], repeat=6):
#     table = [
#         (a[0], 0, 0, 0 ),
#         (a[1], a[2], 0, 0),
#         (a[3], a[4], 0, a[5])
#     ]
#     if len(table) == len(set(table)):
#         for porydok in permutations ('xywz'):
#             if [f(**dict(zip(porydok, r))) for r in table] == [0,0,0]:
#                 print(''.join(porydok))
# from turtle import *
# tracer(0)
# pensize(5)
# k = 15
# screensize(5000, 5000)
# lt(90)
# for i in range(2):
#     fd(24*k)
#     rt(90)
#     fd(10*k)
#     rt(90)
#
# fd(3*k)
# lt(90)
# fd(13*k)
# rt(90)
#
# for j in range(2):
#     fd(9*k)
#     rt(90)
#     fd(32*k)
#     rt(90)
# up()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x*k, y*k)
#         dot(5, 'red')
# done()

# f = open(r'C:\Users\s-ea.kravtsova\PycharmProjects\pythonProject\9.txt')
# data = [
#     [int(i) for i in row.split()] for row in f
# ]
# index = 0
# res = [[],[]]
# mn = 300000
# def check(row):
#     uni = []
#     povtor = []
#     srow = sorted(row)
#     for num in row:
#         if row.count(num) == 1:
#             uni.append(num)
#         if row.count(num) == 3:
#             povtor.append(num)
#     return len(uni) == 4 and len(povtor) == 3 and povtor[0] <= int(sum(uni))//4 and int(srow[-1])%int(srow[0]) != 0
#
# for row in data:
#     index += 1
#     if check(row):
#         res.append(sum(row), index)

# print(min(res[0]))

# for a in range(1, 10000):
#     flag = True
#     for x in range(1, 10000):
#         if not(
#             (x&51 == 0) or
#             ((x&41==0) <= ((x&a)==0) )
#         ):
#             flag = False
#     if flag:
#         print(a)
# # #
# def f19(s, step=1): #1p 2v 3p 4v 5p
#     if (step ==5) and s <= 19:
#         return 1
#     if (
#         ((step ==5) and (s <= 19)) or
#         ((step ==5) and (s>19))
#     ):
#         return 0
#     moves = [
#         f19(s-2, step+1),
#         f19(s-5, step+1),
#         f19(s//3, step+1)
#     ]
#     if step%2 == 1:
#         return all(moves)
#     return any(moves)
#
# for s in range(20, 300):
#     if f19(s):
#         print(s)



# k = 0
# res = []
# for x in range(2, 2025):
#     num = 5**2025+5**200-x
#     while num>0:
#         if num%5 == 4:
#             k += 1
#         num //= 5
#     res.append(k)
#     if k == 396839:
#         print(x)
# network = '98.162.71.64'
# # mask
# ip = '98.167.71.94'
# bin_net = [bin(int(i))[2:].zfill(8) for i in network.split('.')]
# bin_ip = [bin(int(i))[2:].zfill(8) for i in ip.split('.')]
#
# print(bin_net)
# print(bin_ip)
# ['01100010', '10100010', '01000111', '010 00000']
# ['01100010', '10100111', '01000111', '010 11110']
# left = '01100010101001110100011101'
# for i in range(1, 2**5):
#     right = bin(i)[2:].zfill(5)
#     print(right+left)
#     break
#
# print(int('01100010',2))
# print(int('10100111',2))
# print(int('01000111',2))
# print(int('00111010',2))




# f = open(r'C:\Users\s-ea.kravtsova\PycharmProjects\pythonProject\17.txt').read()
#
#




def f19(s, step=1): #1p 2v 3p 4v 5p
    if (step in (3,)) and s <= 19:
        return 1
    if (
        ((step < 3) and (s <= 19)) or
        ((step == 3) and (s>19))
    ):
        return 0
    moves = [
        f19(s-2, step+1),
        f19(s-5, step+1),
        f19(s//3, step+1)
    ]
    if step%2 == 1:
        return all(moves)
    return any(moves)

for s in range(20, 300):
    if f19(s):
        print(s)



64
67
68
186
187