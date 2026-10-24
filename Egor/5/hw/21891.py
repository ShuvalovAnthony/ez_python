answer=[]
for n in range (1,10000):
    n_2=bin(n)[2:]
    n_2+=str(n_2.count('1') % 2) 
    n_2+=str(n_2.count('1') % 2) 
    r=int(n_2,2)
    if r>253:
        answer.append(n)
print(min(answer))