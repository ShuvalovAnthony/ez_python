f = open("Evgenii/17/19249/17_19249.txt")


nums = [int(i) for i in f]


for num in sorted(nums, reverse=True):
    if (
        (10_000 <= abs(num) <= 99999) and
        (abs(num)%100 == 43) # str(num)[-2:] == '43'
    ):
        kv_max_num = num**2
        break



def check(triplet: list):
    if sum([i**2 for i in triplet]) > kv_max_num:
        return False
    
    for num in triplet:
        if (
            (10_000 <= abs(num) <= 99999) and
            (abs(num)%100 == 43)
        ):
            return True
    
    return False


counter = 0
min_summa_kv = 10**12

for i in range(len(nums) - 2):
    triplet = [nums[i], nums[i + 1], nums[i + 2]]

    if check(triplet):
        counter += 1
        min_summa_kv = min(
            min_summa_kv, 
            sum([i**2 for i in triplet])
            )
        
print(counter, min_summa_kv)
