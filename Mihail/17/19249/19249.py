f = open("Mihail/17/19249/17_19249.txt")

nums = [int(i) for i in f]

for num in sorted(nums, reverse=True):
    if (
        (10_000 <= abs(num) <= 99_999) and
        (abs(num)%100 == 43)
    ):
        kv_max_ok_na_43 = num**2
        break


def check(troika: list):
    counter = 0

    for num in troika:
        if (
            (10_000 <= abs(num) <= 99_999) and
            (abs(num)%100 == 43)
        ):
            counter += 1

    return (
        (counter == 1) and
        (sum([i**2 for i in troika]) <= kv_max_ok_na_43)
    )

count = 0
min_sum_kv = 10**10

for i in range(len(nums) - 2):
    troika = nums[i:i + 3]

    if check(troika):
        count += 1
        min_sum_kv = min(min_sum_kv, sum([i**2 for i in troika]))

print(count, min_sum_kv)