a = int(input())
summ = 0
while a!=0:
    if (a%4 == 0) or (a%9 == 0): 
         summ +=a
    a = int(input())
print(summ)