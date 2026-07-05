def to_7(num):
    res = ''

    while num > 0:
        res += str(num%7)
        num //= 7

    return res[::-1]

nums = []

while True:
    num = int(input())

    if num == 0: break

    num_7 = to_7(num)
    
    if num_7[-1] == '3':
        nums.append(num)


if nums:
    print(sum(nums))
else:
    print("NO")