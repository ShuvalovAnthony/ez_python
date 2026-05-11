f = open("Danya/17/28938/17_28938.txt")

nums = [int(i) for i in f]

for num in sorted(nums):
    if str(num)[-2:] == "28":
        max_na_28 = num


def check(troika: list):
    k = 0 # kolvo trehznachnih
    for num in troika:
        if 100 <= abs(num) <= 999:
            k += 1
    
    sr_ar = sum(troika)/3

    return (
        (k >= 1) and
        (sr_ar > 0) and
        (sr_ar < max_na_28)
    )


counter = 0
max_sum = 0


for i in range(len(nums) - 2):
    troika = nums[i:i + 3]

    if check(troika):
        counter += 1

        max_sum = max(max_sum, sum(troika))


print(counter, max_sum)