f = open("Polina/17/21903/17_21903.txt")

nums = [int(i) for i in f]



for num in sorted(nums):
    if (abs(num)%100 == 15) and (100 <= abs(num) <= 999):
       kv_min_el = num**2


def check(troika: list):
    positive = 0
    negative = 0

    for num in troika:
        if num < 0: negative += 1
        if num >= 0: positive += 1

    return (
        ((positive == 3) or (negative == 3)) and
        (min(troika)*max(troika) > kv_min_el)
    )


counter = 0
min_proizv = 10**10


for i in range(len(nums) - 2):
    troika = nums[i:i + 3]

    if check(troika):
        counter += 1
        min_proizv = min(min_proizv,
                         min(troika)*max(troika))
                         
                         
print(counter, min_proizv)