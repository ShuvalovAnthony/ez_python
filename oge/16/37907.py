answ = 10**6

while True:
    num = int(input())
    if num == 0:
        break
    
    if (num%3 == 0) and (num < answ):
        answ = num

print(answ)

