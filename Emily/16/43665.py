summa = 0

while True:
    num = int(input())

    if num == 0:
        break

    if (100 <= num <= 999) and (num%4 == 0):
        summa = summa + num


print(summa)
    