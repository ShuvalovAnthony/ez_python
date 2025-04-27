f = open("Alexander_/17/19749/17_19749.txt")


nums = [int(i) for i in f]



ost_na_3 = min(nums)%3
ost_na_7 = max(nums)%7


def check(troika: list):
    res_1 = [i for i in troika if i%3 == ost_na_3]
    res_2 = [i for i in troika if i%7 == ost_na_7]

    return (
        (len(res_1) == 1) and (len(res_2) >= 2)
    )


counter = 0
max_summa = 0


for i in range(len(nums) - 2):
    troika = [nums[i], nums[i + 1], nums[i + 2]]

    if check(troika):
        counter += 1
        max_summa = max(max_summa, sum(troika))


print(counter, max_summa)