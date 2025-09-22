from re import findall

f = open(r'Katia/24/21908/24_21908.txt').read()

pattern = r'([1-9A-D][1-9A-D]*[02468AC])'
nums = findall(pattern, f)


nums = sorted(nums, key=lambda x: [-len(x),int(x,14)])

answ = nums[0]

print(len(answ))