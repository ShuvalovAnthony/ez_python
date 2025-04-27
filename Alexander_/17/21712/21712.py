f = open("Alexander_/17/21712/17_21712.txt")

nums = [int(i) for i in f]


for num in sorted(nums):
    if num > 0:
        if (1000 <= num <= 9999) and (num%10 == 6):
            min_na_6 = num
            break


def check(troika: list):
    usl1 = 0
    for num in troika:
        if (
            (1000 <= abs(num) <= 9999) and
            (abs(num)%10 == 6)
        ):
            usl1 += 1

    return (
        (usl1 == 1) and
        (sum(troika) <= min_na_6)
    )


counter = 0
max_summa = 0

# подряд
for i in range(len(nums) - 2):
    troika = [nums[i], nums[i + 1], nums[i + 2]]

    if check(troika):
        counter += 1
        max_summa = max(max_summa, sum(troika))

print(counter, max_summa)




#  каждое с каждым (давно не было)
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         for k in range(j + 1, len(nums)):
#             troika = [nums[i], nums[j], nums[k]]
#             print(troika)