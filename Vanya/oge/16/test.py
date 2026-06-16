def to_7(num):
    res = ''

    while num > 0:
        res += str(num%7)
        num //= 7

    return res[::-1]


n = int(input())
summa = 0

for i in range(n):
    num = int(input())

    if to_7(num)[-1] == '1':
        summa += num


print(summa)