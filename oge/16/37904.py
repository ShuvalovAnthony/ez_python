counter = 0

while True:
    num = int(input())
    if num == 0: break
    # num in range(100, 1000)
    if (100 <= num <= 999) and (num%4 == 0):
        counter += 1


print(counter)