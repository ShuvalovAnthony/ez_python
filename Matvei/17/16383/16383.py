f=open('Matvei/17/16383/17_16383.txt')

nums=[int(i) for i in f]
el=[]

for num in nums:
    if (abs(num) % 100 == 21) and (99999 >= abs(num) >= 10000):
        el.append(num)
max_el=max(el)



def check(pair:list):
    spusok=[]
    if (abs(num) % 100 == 21) and (99999 >= abs(num) >= 10000):
        spusok.append(num)
    return ((max_el**2)<=sum([i**2 for i in pair])) and (len(spusok)==1)

counter = 0
max_sum = 0

for i in range(len(nums) - 1):
    pair = [nums[i], nums[i + 1]]
    if check(pair):
        counter += 1
        max_sum = max(max_sum, sum(pair))
print(counter, max_sum)