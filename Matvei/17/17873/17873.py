f = open("Matvei/17/17873/17_17873.txt")


nums = [int(i) for i in f]


min_el = min(nums)


def check(pair: list):
    return (
        (pair[0]%16 == min_el) or
        (pair[1]%16 == min_el)
    )



counter = 0
max_sum = 0


for i in range(len(nums) - 1):
    pair = [nums[i], nums[i + 1]]

    if check(pair):
        counter += 1
        max_sum = max(max_sum, sum(pair))

print(counter, max_sum)