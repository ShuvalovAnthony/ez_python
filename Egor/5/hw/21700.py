def to_3(n: int):
    res=''
    while n>0:
        res+=str(n%3)
        n//=3
    res=res[::-1]
    return res
answer=[]
for n in range (1,10000):
    n_3=to_3(n)
    if n%3==0:
        n_3+=n_3[:2]
    else:
        n_3+=to_3((n%3)*3)
    r=int(n_3,3)
    if r<=150:
        answer.append(n)
print(max(answer))