n = int(input())

summa = 0

for i in range(n):
    num = int(input()) # int

    num_7 = '' # str
    while num > 0:
        num_7 += str(num%7)
        num //= 7

    num_7 = num_7[::-1] # str

    if num_7[-1] == '1':
        summa += int(num_7, 7)


print(summa)