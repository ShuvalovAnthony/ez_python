# 1 sposob
counter = 0

for x in range(10, 100):
    if (
        (not x%2 == 1) and
        (not x > 51)
    ):
        counter += 1


print(counter)

# 2 sposob
nums = []

for x in range(10, 100):
    if (
        (not x%2 == 1) and
        (not x > 51)
    ):
        nums.append(x)


print(len(nums))