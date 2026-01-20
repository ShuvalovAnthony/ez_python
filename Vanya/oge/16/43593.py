# функция перевода в 7ричную
def to_7(num):
    res = ''

    while num > 0:
        res = str(num%7) + res
        num //= 7

    return res # str

nums = []

n = int(input())

for i in range(n):
    num = int(input())

    if to_7(num)[-1] == '5':
        nums.append(num)


if nums:
    print(sum(nums)/len(nums))
else:
    print("NO")
