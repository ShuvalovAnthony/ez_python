n = int(input())

summa = 0

for i in range(n):
    num = int(input())

    if (num%6 == 0) and (num%10 == 4):
        summa = summa + num


print(summa)
