f = open("Alexander/17/19249/17_19249.txt")

nums = [int(i) for i in f]


kv_max_ok_na_43 = 0

for num in sorted(nums, reverse=True):
    num = abs(num)
    if (10_000 <= num < 100_000) and (num%100 == 43):
        kv_max_ok_na_43 = max(
            kv_max_ok_na_43, 
            num**2
        )
        break


count = 0
min_summ_kv = 10**10


def check(triple: list):
    for num in triple:
        num = abs(num)
        if (10_000 <= num < 100_000) and (num%100 == 43):
            return True
    return False


for i in range(len(nums) - 2):
    triple = [nums[i], nums[i + 1], nums[i + 2]]
    if (
        check(triple) and
        (sum([i**2 for i in triple]) <= kv_max_ok_na_43)
    ):
        count += 1
        min_summ_kv = min(min_summ_kv, sum([i**2 for i in triple]))


print(count, min_summ_kv)
