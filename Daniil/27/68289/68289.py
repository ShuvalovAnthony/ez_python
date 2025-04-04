f = open("Daniil/27/68289/27-B.txt")

n = int(f.readline())

nums = [int(i) for i in f]

nums = [i for i in nums if i >= 99984034]

max_sum = 0

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            a, b, c = nums[i], nums[j], nums[k]
            if a > b > c:
                max_sum = max(max_sum, a + b + c)


print(max_sum)