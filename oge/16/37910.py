k = int(input())
summa = 0


for _ in range(k):
    num = int(input())

    if num%6 == 0:
        summa += num


print(summa)
