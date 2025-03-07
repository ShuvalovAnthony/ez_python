f = open("Daniil/17/63066/63066.txt")


nums = [int(i) for i in f]


max_ok_na_321 = 0
for num in sorted(nums, reverse=True):
    # if str(num)[-3:] == "321":
    #     max_ok_na_321 = num
    #     break
    
    if num%1000 == 321:
        max_ok_na_321 = num
        break


def check(nums: list):
    pyatiznach = 0
    for num in nums: pyatiznach += num in range(10**4, 10**5)
    if pyatiznach != 2: return False

    div_by_5 = 0
    for num in nums:
        if num%5 == 0:
            div_by_5 += 1
    if div_by_5 == 0: return False

    return sum(nums) > max_ok_na_321


counter = 0
max_summa = 0


for i in range(len(nums) - 2):
    if check([nums[i], nums[i + 1], nums[i + 2]]):
        counter += 1
        max_summa = max(max_summa, nums[i] + nums[i + 1] + nums[i + 2])


print(counter, max_summa)