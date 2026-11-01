from itertools import product
index=1
count=0

def check(num: str):
    for digit in '0123456789ABC':
        if digit*2 in num:
            return False

    return True


for number in product(sorted('0123456789ABC'), repeat=5):
    number=''.join(number)
    if number.count('0')==1 and number[0]!='0' and check(number):
        count+=1
    index+=1
print(count)
