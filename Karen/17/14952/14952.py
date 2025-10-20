f = open("Karen/17/14952/17_14952.txt")

nums = [int(i) for i in f]

# максимального элемента последовательности, оканчивающегося на 121
for num in sorted(nums, reverse=True):
    if abs(num)%1000 == 121:
        max_el_ok_na_121 = num
        break


def check(troika: list):
    k = 0
    for num in troika:
        if (1000 <= abs(num) <= 9999) and (abs(num)%2 == 0):
            k += 1

    return (
        (k <= 1) and
        (sum(troika) <= max_el_ok_na_121)
    )


counter = 0
max_sum = 0

for i in range(len(nums) - 2):
    troika = nums[i:i + 3]
    
    if check(troika):
        counter += 1
        max_sum = max(max_sum, sum(troika))

print(counter, max_sum)