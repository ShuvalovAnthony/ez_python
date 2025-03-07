f = open("Daniil/17/17.txt")


nums = [int(i) for i in f]


ost_na_5_max_el = max(nums)%5
ost_na_7_min_el = min(nums)%7


counter = 0
max_summa = 0


def check(triplet):
    # 1 uslov
    chetirehZnach = 0
    for num in triplet:
        if num in range(10**3, 10**4): chetirehZnach += 1
    if chetirehZnach == 0: return False

    # 2 uslov
    counter_ostatkov_na_5 = 0
    for num in triplet:
        if num%5 == ost_na_5_max_el: counter_ostatkov_na_5 += 1
    if counter_ostatkov_na_5 > 1: return False


    # 3 uslo
    counter_ostatkov_na_7 = 0
    for num in triplet:
        if num%7 == ost_na_5_max_el: counter_ostatkov_na_7 += 1
    if counter_ostatkov_na_7 < 2: return False

    return True


for i in range(len(nums) - 2):
    if check([nums[i], nums[i + 1], nums[i + 2]]):
        counter += 1
        max_summa = max(max_summa, nums[i] + nums[i + 1] + nums[i + 2])



print(counter, max_summa)