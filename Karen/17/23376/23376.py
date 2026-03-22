f = open("Karen/17/23376/17_23376.txt")

nums = [int(i) for i in f]

for num in sorted(nums):
    if 10_000 <= abs(num) <= 99_999 and abs(num)%100 == 37:
        kv_max_na_37 = num**2

def check(row: list):
    k = 0 # колво пятизначных
    for num in row:
        if 10_000 <= abs(num) <= 99_999:
            k += 1

    return (
        (k == 1) and
        (sum(row)**2 > kv_max_na_37)
    )

counter = 0
max_sum = 0


for i in range(len(nums) - 1):
    row = nums[i: i + 2]

    if check(row):
        counter += 1
        max_sum = max(max_sum, sum(row))


print(counter, max_sum)