def prostota(n):
    fl=True
    for i in range(2,int(n**0.5) + 1):
        if n%i==0:
            fl=False
            break
    return fl

def check(n):
    deliteli=[]
    pr_del=[]
    for i in range(2,int(n**0.5) + 1):
        if n%i==0:
            deliteli.append(i)
            deliteli.append(n//i)

    for i in deliteli:
        if prostota(i):
            pr_del.append(i)
    pr_del.sort()
    if len(pr_del)>=4 and (pr_del[0]+pr_del[1]+pr_del[-1]+pr_del[-2])%114==39:
        return (pr_del[0]+pr_del[1]+pr_del[-1]+pr_del[-2])
    return False
    

counter=0
for n in range(456_790,1_000_000):
    res=check(n)
    if res:
        print(n,res)
        counter+=1
    if counter==5:
        break