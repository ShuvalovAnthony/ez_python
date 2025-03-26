from itertools import product


answ = 0

for num in product(range(12), repeat=5):
    
    counter = len([i for i in num if i > 8])
    
    if (counter <= 3) and (num.count(7) == 1) and (num[0] != 0):
        answ += 1

print(answ)
