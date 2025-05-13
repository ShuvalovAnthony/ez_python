f = open("Matvei/17/14255/17_14255.txt")

nums = [int(i) for i in f]


temp_list = [i for i in nums if i%2]

avg = sum(temp_list)/len(temp_list)


def check(pair: list):
    ok_na_11 = [i for i in pair if abs(i)%100 == 11]
    
    return (
        (len(ok_na_11) == 1) and
        sum(pair) >= avg
    )


counter = 0
max_sum = 0

for i in range(len(nums) - 1):
    pair = [nums[i], nums[i + 1]]

    if check(pair):
        counter += 1
        max_sum = max(max_sum, sum(pair))


print(counter, max_sum)