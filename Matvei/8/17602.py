from itertools import*
cnt=0
for x in product(sorted('0123456789abcd'), repeat=5):
    f=''.join(x)
    counter = 0
    for num in('bcd'):
        counter += x.count(num)

    if (f.count('9')==1) and (counter <= 3) and x[0]!= "0":
        cnt+=1
print(cnt, f)