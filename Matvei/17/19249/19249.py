f = open("Matvei/17/19249/17_19249.txt")


nums = [int(i) for i in f]


for num in sorted(nums, reverse=True):
    if (
        (10_000 <= abs(num) <= 99_999) and
        (abs(num)%100 == 43)
    ):
        kv_max = num**2
        break


def check(troika: list):
    usl1 = 0

    for num in troika:
        if (
            (10_000 <= abs(num) <= 99_999) and
            (abs(num)%100 == 43)
        ):
            usl1 += 1

    return (
        usl1 and
        (sum([i**2 for i in troika]) <= kv_max)
    )



counter = 0
min_summa_kv = 10**10


for i in range(len(nums) - 2):
    troika = nums[i:i + 3]

    if check(troika):
        counter += 1
        min_summa_kv = min(min_summa_kv, sum([i**2 for i in troika]))
    

print(counter, min_summa_kv)