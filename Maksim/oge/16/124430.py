a = int(input())
b = int(input())

nums = []


for num in range(a, b + 1):
    if num%2 == 0:
        nums.append(num)

print(len(nums))

print(nums)