f = open("Daniil/17/56545/17.txt")


nums = [int(i) for i in f]


min_kv_na_7 = 0

for num in sorted(nums): # vosrast
    if str(num)[-1] == "7":
        min_kv_na_7 = num**2
        break

counter = 0
max_summa_kv = 0



def check(num1, num2):
    if str(num1)[-1] != str(num2)[-1]: return False

    if num1**2 + num2**2 > min_kv_na_7: return False

    return (
        ((abs(num1)%7 == 0) and (abs(num2)%7 != 0)) or
        ((abs(num2)%7 == 0) and (abs(num1)%7 != 0))
    )


for i in range(len(nums) - 1):
    if check(nums[i], nums[i + 1]):
        counter += 1
        max_summa_kv = max(max_summa_kv, nums[i]**2 + nums[i + 1]**2)


print(counter, max_summa_kv)