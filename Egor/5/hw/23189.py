answer=[]
for n in range(1,10000):
    n_2 = bin(n)[2:]
    if n%3==0:
        n_2+=n_2[-3:]
    else:
        n_2+=bin((n%3)*3)[2:]
    r=int(n_2, 2)
    if r<130:
        answer.append(n)
print(max(answer))