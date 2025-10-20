f = open("Karen/17/16328/17_16328.txt")

nums = [int(i) for i in f]

for num in sorted(nums): 
    if num%19 == 0:
        min_krat_19 = num
        break


def check(pair: list):
    k = 0
    for num in pair:
        if num%min_krat_19 == 0:
            k += 1

    return k >= 1



counter = 0
max_sum = 0


for i in range(len(nums) - 1):
    pair = nums[i:i + 2]

    if check(pair):
        counter += 1
        max_sum = max(max_sum, sum(pair))

print(counter, max_sum)