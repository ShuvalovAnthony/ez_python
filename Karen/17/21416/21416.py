f = open(r'Karen/17/21416/17_21416.txt')

nums = [int(i)for i in f]

sum_negative = sum([x for x in nums if x < 0])

def check(row: list):
    min_triple = min(row)
    max_trilpe = max(row)

    return(
        (min_triple*max_trilpe > sum_negative)
    )

counter = 0
max_sum = 0

for i in range(len(nums) - 2):
    row = nums[i:i+3]

    if check(row):
        counter += 1
        max_sum = max(max_sum, sum(row))

print(counter, abs(max_sum))