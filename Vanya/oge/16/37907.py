min_number = 10**6

while True:
    number = int(input())

    if number == 0:
        break

    if number < min_number and number%3 == 0:
        min_number = number

print(min_number)