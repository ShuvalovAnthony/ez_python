num = '12432895435fff'

summa_cifr = sum([int(i, 16) for i in num])

print(summa_cifr)

def summa_cifr(num: str):
    summa = 0

    for digit in num:
        summa += int(digit)

    return summa