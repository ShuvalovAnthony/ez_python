f = open("Katia/17/21416/17_21416.txt")


nums = [int(i) for i in f]

summa_negative = sum([i for i in nums if i < 0])

def check(triplet: list):
    return (max(triplet)*min(triplet) > summa_negative)


counter = 0
max_summa = 0

for i in range(len(nums) - 2):
    triplet = [nums[i], nums[i + 1], nums[i + 2]]

    if check(triplet):
        counter += 1
        max_summa = max(max_summa, sum(triplet))


print(counter, max_summa)