f = open("Katia/17/19249/17_19249.txt")

nums = [int(i) for i in f]



for num in sorted(nums, reverse=True):
    if (
        10_000 <= abs(num) <= 99_999 # abs(num) in range(10**4, 10**5)
    ) and (
        abs(num)%100 == 43 # str(num)[-2:] == '43'
    ):
        kv_max_na_43 = num**2
        break



def check(triplet: list):
    return (
    (
        [i for i in triplet if (
            (10000 <= abs(i) <= 99999) and
            (abs(i)%100 == 43)
    )]
    ) and
    (
        sum([i**2 for i in triplet]) <= kv_max_na_43
    )
    )


counter = 0
min_summa_kv = 10**12


for i in range(len(nums) - 2):
    triplet = [nums[i], nums[i + 1], nums[i + 2]]

    if check(triplet):
        counter += 1
        min_summa_kv = min(min_summa_kv, sum([i**2 for i in triplet]))



print(counter, min_summa_kv)