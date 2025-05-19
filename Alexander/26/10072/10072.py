f = open("Alexander/26/10072/26_10072.txt")

n = int(f.readline())

nums = sorted([int(i) for i in f])

def check(troika: list):
    troika = sorted(troika)
    return troika[0] + troika[1] > troika[2]

counter = 0

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            troika = [nums[i], nums[j], nums[k]]

            counter += check(troika)


    if i%10 == 0:
        print(i)

print(counter)

