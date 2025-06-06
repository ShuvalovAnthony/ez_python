f=open('Evgenii/26/22605/26_22605.txt')

n=f.readline()

data=[[int(i) for i in row.split()] for row in f]

base={}

for row in data:
    koord=(row[0],row[1])
    t=row[2]

    if koord in base:
        base[koord].add(t)
    else:
        base[koord]={t}

def check(row):
    li=[]
    for i in row:
        li.append(i)
    min_prom=10**10
    li.sort()
    for i in range(len(li)-1):
        min_prom=min(min_prom,li[i+1]-li[i])

    return min_prom

otvet=[]

for i in base.keys():
    if len(base[i])>1:
        otvet.append([check(base[i]),i[0],i[1]])
        

otvet=sorted(otvet,key=lambda x:(
    -x[0],
    -x[1],
    -x[2]
))

# otvet=sorted(otvet,reverse=True)

for i in otvet:
    print(i)