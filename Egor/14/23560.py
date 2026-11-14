def to_9 (n:int):
    res=''
    while n>0:
        res+=str(n%9)
        n//=9
    return res[::-1]
 
amount=[]

for x in range(1, 2401):
    exp=7*9**210+6*9**110-x
    exp_9=to_9(exp)
    if exp_9.count('0') == 100:
        amount.append(x)
print(max(amount))