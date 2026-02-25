f = open("Danya/17/23757/17_23757.txt")


nums = [int (i) for i in f]

for num in sorted(nums):
    if (
        num in range(10, 100)
    ):
        num_2 = num
        break


def check(dvoyka: list):
    k = 0
    for num in dvoyka:
        if (
            num in range(10, 100)
        ):
            k+= 1
    return (
        (k == 1) and sum(dvoyka)%num_2 == 0
    )

counter = 0
max_sum = 0

for i in range(len(nums) - 1):
    dvoyka = nums[i: i +2]

    if check(dvoyka):
        counter += 1
        max_sum = max(max_sum, sum(dvoyka))

print(counter, max_sum)