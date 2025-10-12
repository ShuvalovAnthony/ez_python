nums = []

while True:
    num = int(input())

    if num == 0:
        break

    if (num%3 == 0) and (num%2 == 0):
        nums.append(num)

print(len(nums))