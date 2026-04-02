summa = 0

while True:
    number = int(input())

    if number == 0:
        break

    if (100 <= number <= 999) and (number%4 == 0):
        summa += number

print(summa)