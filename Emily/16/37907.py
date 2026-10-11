min_num = 10**6

while True:
    num = int(input())

    if num == 0:
        break

    if (num%3 == 0) and (num < min_num):
        min_num = num


print(min_num)