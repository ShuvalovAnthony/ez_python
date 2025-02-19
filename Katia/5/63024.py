from itertools import product

counter = 0 

def check(num:str):
    for i in set(num):
        if num.count(i)> 4: return False 
    return True

odd = "1357"
even = "2468"

for num in product(odd, even, odd, even, odd, even, odd, even, odd, even, odd):
    num = "".join(num)
    if check(num):
        counter += 1

print(counter*2)
