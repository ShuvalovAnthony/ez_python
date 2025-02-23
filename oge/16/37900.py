nums = []

while True:
    num = int(input())
    if num == 0: break

    if num%8 == 0:
        nums.append(num)


if nums:
    print(sum(nums)/len(nums))
else:
    print("NO")
