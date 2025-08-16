s = "1 4 5 5 5 99 88 77 33 12 9 3 3 5 5 5"

nums = []

for num in s.split():
    nums.append(int(num))

print(nums)

answ = 0
counter = 0

for num in set(nums):
    if nums.count(num) > counter:
        answ = num
        counter = nums.count(num)

print(answ)