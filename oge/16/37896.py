k = int(input())

nums = []


for i in range(k):
    num = int(input())

    if num%3 == 0:
        nums.append(num)


print(min(nums))