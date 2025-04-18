f = open("Katia/17/17558/17_17558.txt")


nums = [int(i) for i in f]


krat_32 = len([i for i in nums if i%32 == 0])


def check(pair: list):
    return (
        ((pair[0] < 0) or (pair[1] < 0)) and
        (sum(pair) < krat_32)
    )


counter = 0
max_summa = 0


for i in range(len(nums) - 1):
    pair = [nums[i], nums[i + 1]]

    if check(pair):
        counter += 1
        max_summa = max(max_summa, sum(pair))


print(counter, max_summa)