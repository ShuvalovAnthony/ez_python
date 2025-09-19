from re import findall


f = open("Katia/24/22361/24_22361.txt").read()

pattern = r"([1-B][0-7]*[0246])"
nums = findall(pattern, f)

# lambda x: len(x) - это то же самое, что и
# for x in nums:
#     сортировать по len(x)
# x - элемент списка

nums = sorted(nums,key=lambda x:[-len(x), int(x, 12)])

answ = nums[0]

for num in nums[:20]:
    print(num, len(num), int(num, 12))

print(f.index(answ))