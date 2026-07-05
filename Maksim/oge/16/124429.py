k = int(input())

count = 0

for i in range(k):
    minutes, sec = [int(i) for i in input().split()]

    if (minutes*60 + sec) <= (18*60 + 30):
        count += 1


print(count)